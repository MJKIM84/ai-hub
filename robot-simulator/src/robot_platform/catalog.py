"""Model definitions: synthetic research parameters are never product specifications."""
from copy import deepcopy


_MODELS = [
    dict(id="spot", name="Boston Dynamics Spot", kind="quadruped", locomotion="legs", size=dict(x=1.1,y=0.55,z=0.65), mass=50.34, max_payload=0, max_speed=1.0, capabilities=["patrol", "inspect"], source="Menagerie BSD-3-Clause; original source and commit in assets/robots/spot", limitations=["모델 질량은 MJCF 값이며 제조사 실측 사양이 아님", "실제 제조사 제어기와 다름", "계단·경사로 능력은 실행 시험 전 미검증", "기본형은 물체 조작 불가"]),
    dict(id="delivery", name="배송 로봇 · 연구 모델", kind="delivery", locomotion="differential", size=dict(x=0.65,y=0.5,z=0.65), mass=25, max_payload=10, max_speed=0.6, capabilities=["patrol", "delivery", "transport", "retrieve"], source="Platform authored parametric research model", limitations=["제품 모델이 아닌 일반 연구용 동역학", "계단 통행 불가"]),
    dict(id="amr", name="AMR · 연구 모델", kind="amr", locomotion="differential", size=dict(x=0.8,y=0.65,z=0.4), mass=45, max_payload=50, max_speed=0.7, capabilities=["patrol", "transport", "retrieve"], source="Platform authored parametric research model", limitations=["적재량은 연구용 설정이며 실물 인증값 아님"]),
    dict(id="agv", name="AGV · 연구 모델", kind="agv", locomotion="guided", size=dict(x=0.9,y=0.65,z=0.4), mass=60, max_payload=80, max_speed=0.5, capabilities=["transport", "patrol"], source="Platform authored guided-route research model", limitations=["설정된 지정 경로를 사용", "계단 통행 불가"]),
    dict(id="logistics", name="물류 운반 로봇 · 연구 모델", kind="logistics", locomotion="differential", size=dict(x=1.0,y=0.75,z=0.55), mass=85, max_payload=120, max_speed=0.45, capabilities=["transport", "delivery", "retrieve"], source="Platform authored heavy transport research model", limitations=["상하차는 물리적 적재 장치/협업 동작 검증이 필요"]),
    dict(id="arm", name="고정형 로봇팔 · 연구 모델", kind="arm", locomotion="fixed", size=dict(x=0.7,y=0.7,z=1.3), mass=30, max_payload=3, max_speed=0, capabilities=["load", "unload", "manipulate", "handoff"], source="Platform authored articulated research arm", limitations=["작업 반경 내 조작만 가능", "물리 파지/인계 검증 진행 중"]),
    dict(id="mobile_manipulator", name="이동형 조작 로봇 · 연구 모델", kind="mobile_manipulator", locomotion="differential", size=dict(x=0.85,y=0.65,z=1.4), mass=60, max_payload=3, max_speed=0.4, capabilities=["patrol", "transport", "load", "unload", "manipulate", "handoff"], source="Platform authored mobile articulated research model", limitations=["이동 기반과 관절 팔의 결합", "제조사 제품 검증을 의미하지 않음"]),
]


def _describe(raw: dict) -> dict:
    model = deepcopy(raw)
    model["support"] = {"model": "제공", "simulation": "진행 중", "contract": "진행 중" if model["id"] == "spot" else "미검증", "hardware": "미검증"}
    model["parameter_basis"] = "upstream MJCF" if model["id"] == "spot" else "명시적 연구용 가정"
    runnable={"patrol"}
    if model["id"] in ("arm","mobile_manipulator"):runnable.add("manipulate")
    model["capability_status"]={kind:("조건부 실행" if kind in runnable else "실행 검증 대기") for kind in model["capabilities"]}
    if model["id"]=="spot":
        model["limitations"][2]="평지 주행 1.0m/s 연구 상한; 제조사 최대 1.6m/s와 구분. 계단·경사 재검증 필요"
    if model["id"] in ("arm","mobile_manipulator"):
        model["limitations"].append("1·3kg 정렬 상자의 정지 차체 파지·놓기 검증; 협업 인계는 미완료")
    if model["id"]=="arm":model["limitations"][1]="작업 반경과 물품 관측 조건을 만족해야 조작 실행 가능"
    return model


def models() -> list[dict]:
    return [_describe(model) for model in _MODELS]


def model_by_id(model_id: str) -> dict:
    for model in _MODELS:
        if model["id"] == model_id:
            # Enrich/copy only the requested model, not the entire fleet catalog.
            return _describe(model)
    raise ValueError(f"알 수 없는 로봇 모델: {model_id}")


def model_footprint(model_id: str) -> tuple[float, float]:
    """Immutable dimensions for hot path collision checks; no catalog copies."""
    for model in _MODELS:
        if model['id'] == model_id:
            return model['size']['x'], model['size']['y']
    raise ValueError(f"알 수 없는 로봇 모델: {model_id}")
