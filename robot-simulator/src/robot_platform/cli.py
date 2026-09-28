import argparse
import json
from pathlib import Path


def main():
    parser=argparse.ArgumentParser(description="로봇 운영 물리 실험실")
    sub=parser.add_subparsers(dest="action",required=True)
    serve=sub.add_parser("serve");serve.add_argument("--port",type=int,default=8000);serve.add_argument("--host",default="127.0.0.1")
    serve.add_argument("--personal-api",action="store_true",help="방문자별 임시 작업 공간과 개인 API 키 모드")
    run=sub.add_parser("run");run.add_argument("--project",type=Path);run.add_argument("--template",default="hotel");run.add_argument("--duration",type=float,default=10);run.add_argument("--seed",type=int,default=42);run.add_argument("--output",type=Path,default=Path("reports/run.json"))
    args=parser.parse_args()
    if args.action=="serve":
        import uvicorn
        uvicorn.run("robot_platform.visitor_api:create_personal_app" if args.personal_api else "robot_platform.api:create_app",factory=True,host=args.host,port=args.port,access_log=not args.personal_api)
    else:
        from .domain import Project
        from .templates import example
        from .experiments import run_one
        project=Project.model_validate_json(args.project.read_text()) if args.project else example(args.template)
        project.physics.seed=args.seed
        result=run_one(project,args.duration)
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2))
        print(json.dumps(result["metrics"],ensure_ascii=False,indent=2))


if __name__=="__main__":main()
