"""
Azure Function을 사용한 CERT 내부자 위협 분석 통합 예제

이 스크립트는 CERT 분석기를 Azure Functions와 통합하는 방법을 보여줍니다.
Event Hub에서 사용자 행동 데이터를 받아 위협을 분석하고 결과를 반환합니다.
"""

import azure.functions as func
import logging
import json
from cert_analysis import CERTInsiderThreatAnalyzer

app = func.FunctionApp()

# CERT 분석기 초기화 (전역 변수로 재사용)
try:
    cert_analyzer = CERTInsiderThreatAnalyzer(answers_folder="answers")
    logging.info("CERT 분석기 초기화 완료")
except Exception as e:
    logging.error(f"CERT 분석기 초기화 실패: {str(e)}")
    cert_analyzer = None


@app.function_name(name="analyze_user_threat")
@app.route(route="analyze_threat", methods=["POST"], auth_level=func.AuthLevel.FUNCTION)
def analyze_user_threat(req: func.HttpRequest) -> func.HttpResponse:
    """
    HTTP 요청으로 사용자 행동 데이터를 받아 위협을 분석합니다.
    
    요청 형식:
    POST /api/analyze_threat
    {
        "user_id": "USR001",
        "daily_file_access": 1200,
        "unique_files": 600,
        "sensitive_files": 55,
        "external_emails": 120,
        "email_attachment_size_mb": 150,
        "off_hours_logins": 15,
        "failed_logins": 25,
        "data_transfer_gb": 60,
        "external_connections": 250
    }
    
    응답 형식:
    {
        "user_id": "USR001",
        "total_risk_score": 1.0,
        "threat_level": "CRITICAL",
        "alerts": [...],
        "potential_threats": [...]
    }
    """
    logging.info('CERT 위협 분석 함수가 호출되었습니다.')
    
    if not cert_analyzer:
        return func.HttpResponse(
            json.dumps({
                "error": "CERT 분석기가 초기화되지 않았습니다.",
                "status": "failed"
            }, ensure_ascii=False),
            status_code=500,
            mimetype="application/json"
        )
    
    try:
        # 요청 본문 파싱
        req_body = req.get_json()
        logging.info(f"사용자 데이터 수신: {req_body.get('user_id')}")
        
        # 사용자 행동 분석
        analysis_result = cert_analyzer.analyze_user_behavior(req_body)
        
        # 결과 로깅
        logging.info(
            f"분석 완료 - 사용자: {analysis_result['user_id']}, "
            f"위협 수준: {analysis_result['threat_level']}, "
            f"위험 점수: {analysis_result['total_risk_score']}"
        )
        
        # CRITICAL 또는 HIGH 위협인 경우 추가 로깅
        if analysis_result['threat_level'] in ['CRITICAL', 'HIGH']:
            logging.warning(
                f"⚠️ 고위험 사용자 탐지: {analysis_result['user_id']} "
                f"({analysis_result['threat_level']})"
            )
        
        # 결과 반환
        return func.HttpResponse(
            json.dumps(analysis_result, ensure_ascii=False, indent=2),
            status_code=200,
            mimetype="application/json"
        )
        
    except ValueError as e:
        logging.error(f"잘못된 요청 형식: {str(e)}")
        return func.HttpResponse(
            json.dumps({
                "error": "잘못된 요청 형식입니다.",
                "details": str(e)
            }, ensure_ascii=False),
            status_code=400,
            mimetype="application/json"
        )
    except Exception as e:
        logging.error(f"분석 중 오류 발생: {str(e)}")
        return func.HttpResponse(
            json.dumps({
                "error": "분석 중 오류가 발생했습니다.",
                "details": str(e)
            }, ensure_ascii=False),
            status_code=500,
            mimetype="application/json"
        )


@app.event_hub_message_trigger(
    arg_name="azeventhub", 
    event_hub_name="user-behavior-hub",
    connection="EventHubConnection"
)
def eventhub_threat_analyzer(azeventhub: func.EventHubEvent):
    """
    Event Hub에서 사용자 행동 데이터를 받아 실시간으로 위협을 분석합니다.
    
    이벤트 형식:
    {
        "user_id": "USR001",
        "daily_file_access": 1200,
        "unique_files": 600,
        ...
    }
    """
    logging.info('Event Hub에서 사용자 행동 데이터 수신')
    
    if not cert_analyzer:
        logging.error("CERT 분석기가 초기화되지 않았습니다.")
        return
    
    try:
        # 이벤트 데이터 파싱
        event_data = json.loads(azeventhub.get_body().decode('utf-8'))
        user_id = event_data.get('user_id', 'UNKNOWN')
        
        logging.info(f"사용자 {user_id}의 행동 데이터 분석 시작")
        
        # 사용자 행동 분석
        analysis_result = cert_analyzer.analyze_user_behavior(event_data)
        
        # 결과 로깅
        threat_level = analysis_result['threat_level']
        risk_score = analysis_result['total_risk_score']
        
        logging.info(
            f"분석 완료 - 사용자: {user_id}, "
            f"위협 수준: {threat_level}, "
            f"위험 점수: {risk_score}"
        )
        
        # 고위험 사용자인 경우 경고 발송
        if threat_level in ['CRITICAL', 'HIGH']:
            logging.warning(
                f"🚨 고위험 사용자 탐지: {user_id}\n"
                f"위협 수준: {threat_level}\n"
                f"위험 점수: {risk_score}\n"
                f"알림 수: {len(analysis_result['alerts'])}\n"
                f"잠재적 위협: {len(analysis_result['potential_threats'])}건"
            )
            
            # 여기에 알림 로직 추가 가능
            # - 이메일 발송
            # - Slack/Teams 알림
            # - 티켓 생성
            # - 다른 Event Hub로 전송
            send_security_alert(analysis_result)
        
    except json.JSONDecodeError as e:
        logging.error(f"이벤트 데이터 파싱 실패: {str(e)}")
    except Exception as e:
        logging.error(f"분석 중 오류 발생: {str(e)}")


@app.function_name(name="get_historical_analysis")
@app.route(route="historical_analysis", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def get_historical_analysis(req: func.HttpRequest) -> func.HttpResponse:
    """
    과거 위협 데이터 통계를 반환합니다.
    
    GET /api/historical_analysis
    
    응답 형식:
    {
        "total_threats": 10,
        "threat_type_distribution": {...},
        "severity_distribution": {...},
        "resolution_status": {...},
        "monthly_trend": {...}
    }
    """
    logging.info('과거 위협 분석 요청')
    
    if not cert_analyzer:
        return func.HttpResponse(
            json.dumps({
                "error": "CERT 분석기가 초기화되지 않았습니다."
            }, ensure_ascii=False),
            status_code=500,
            mimetype="application/json"
        )
    
    try:
        # 과거 위협 분석
        historical_analysis = cert_analyzer.analyze_historical_threats()
        
        logging.info(
            f"과거 위협 분석 완료 - 총 {historical_analysis['total_threats']}건"
        )
        
        return func.HttpResponse(
            json.dumps(historical_analysis, ensure_ascii=False, indent=2),
            status_code=200,
            mimetype="application/json"
        )
        
    except Exception as e:
        logging.error(f"과거 위협 분석 중 오류 발생: {str(e)}")
        return func.HttpResponse(
            json.dumps({
                "error": "분석 중 오류가 발생했습니다.",
                "details": str(e)
            }, ensure_ascii=False),
            status_code=500,
            mimetype="application/json"
        )


def send_security_alert(analysis_result):
    """
    보안 경고를 발송합니다.
    실제 환경에서는 이메일, Slack, Teams 등으로 알림을 보냅니다.
    """
    user_id = analysis_result['user_id']
    threat_level = analysis_result['threat_level']
    
    # 예: 로깅만 수행 (실제로는 알림 시스템 연동)
    logging.warning(
        f"보안 경고 발송: 사용자 {user_id}, 위협 수준 {threat_level}"
    )
    
    # TODO: 실제 알림 로직 구현
    # send_email(analysis_result)
    # send_slack_notification(analysis_result)
    # create_security_ticket(analysis_result)


# 추가 유틸리티 함수들

@app.function_name(name="batch_analysis")
@app.route(route="batch_analysis", methods=["POST"], auth_level=func.AuthLevel.FUNCTION)
def batch_analysis(req: func.HttpRequest) -> func.HttpResponse:
    """
    여러 사용자의 행동 데이터를 일괄 분석합니다.
    
    요청 형식:
    POST /api/batch_analysis
    {
        "users": [
            { "user_id": "USR001", ... },
            { "user_id": "USR002", ... }
        ]
    }
    """
    logging.info('일괄 분석 요청')
    
    if not cert_analyzer:
        return func.HttpResponse(
            json.dumps({"error": "CERT 분석기가 초기화되지 않았습니다."}),
            status_code=500
        )
    
    try:
        req_body = req.get_json()
        users = req_body.get('users', [])
        
        results = []
        high_risk_count = 0
        
        for user_data in users:
            result = cert_analyzer.analyze_user_behavior(user_data)
            results.append(result)
            
            if result['threat_level'] in ['CRITICAL', 'HIGH']:
                high_risk_count += 1
        
        logging.info(
            f"일괄 분석 완료 - 총 {len(results)}명, "
            f"고위험 사용자 {high_risk_count}명"
        )
        
        return func.HttpResponse(
            json.dumps({
                "total_analyzed": len(results),
                "high_risk_users": high_risk_count,
                "results": results
            }, ensure_ascii=False, indent=2),
            status_code=200,
            mimetype="application/json"
        )
        
    except Exception as e:
        logging.error(f"일괄 분석 중 오류 발생: {str(e)}")
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500
        )


"""
사용 예제:

1. HTTP 요청을 통한 단일 사용자 분석:
   curl -X POST https://your-function-app.azurewebsites.net/api/analyze_threat \
   -H "Content-Type: application/json" \
   -d '{
     "user_id": "USR001",
     "daily_file_access": 1200,
     "unique_files": 600,
     "sensitive_files": 55,
     "external_emails": 120,
     "email_attachment_size_mb": 150,
     "off_hours_logins": 15,
     "failed_logins": 25,
     "data_transfer_gb": 60,
     "external_connections": 250
   }'

2. Event Hub를 통한 실시간 분석:
   - Event Hub에 사용자 행동 데이터를 전송
   - 자동으로 위협 분석이 수행됨
   - 고위험 사용자는 자동으로 알림 발송

3. 과거 위협 통계 조회:
   curl https://your-function-app.azurewebsites.net/api/historical_analysis

4. 일괄 분석:
   curl -X POST https://your-function-app.azurewebsites.net/api/batch_analysis \
   -H "Content-Type: application/json" \
   -d '{
     "users": [
       {"user_id": "USR001", ...},
       {"user_id": "USR002", ...}
     ]
   }'
"""
