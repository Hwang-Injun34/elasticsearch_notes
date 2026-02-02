import pandas as pd
from keybert import KeyBERT
from kiwipiepy import Kiwi
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import CountVectorizer
import torch
import warnings

# ===============================
# 0️⃣ 환경 설정
# ===============================
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# ===============================
# 1️⃣ 모델 로드
# ===============================
model_path = r"C:\Users\ngms0\mini-project\ml_train\ko-sbert"
model = SentenceTransformer(model_path, device=device)
kw_model = KeyBERT(model=model)
kiwi = Kiwi()

# ===============================
# 2️⃣ 국회·법률 문서 전용 불용어 (최종)
# ===============================
CUSTOM_STOPWORDS = set([
    # 인물·직위
    "의원", "대표발의", "발의", "소위원장", "위원장", "위원",
    "전문위원", "차관", "장관", "부장관",

    # 절차·발언
    "보고", "보고드리겠습니다", "말씀", "의견", "동의",
    "다음", "먼저", "이하", "생략", "감사합니다",
    "의사일정", "회의", "심의", "논의",

    # 법률 형식어
    "법률안", "일부개정법률안", "개정법률안", "법안",
    "대안", "원안", "수정", "의결", "심사", "검토",
    "규정", "조항", "내용", "사항",

    # 기관·부처
    "문화체육관광부", "관광부",
    "산업통상부", "산업통상자원부", "산자부",
    "국가유산청", "정부", "부처", "지방자치단체",
    "공단", "위원회",

    # 형식·범용
    "페이지", "쪽", "상단", "하단",
    "제", "조", "항", "호",
    "경우", "등", "관련", "대한"
])

# ===============================
# 3️⃣ Kiwi 기반 커스텀 토크나이저
# ===============================
def kiwi_tokenizer(text):
    tokens = kiwi.analyze(text)
    result = []

    if not tokens:
        return result

    for t in tokens[0][0]:
        # 명사만
        if t.tag not in ["NNG", "NNP"]:
            continue

        # 2글자 이상
        if len(t.form) < 2:
            continue

        # 불용어 제거
        if t.form in CUSTOM_STOPWORDS:
            continue

        # 숫자 제거
        if t.form.isdigit():
            continue

        result.append(t.form)

    return result

# ===============================
# 4️⃣ 테스트 문서
# ===============================
test_docs = [
    "문화예술법안심사소위원회의 소위원장 임오경입니다. 우리 소위원회는 12월 18일 문화체육관광부제1차관 소관 6건 및 국가유산청 소관 2건의 법률안을 심사한 결과 2건을 원안 의결, 2건을 수정 의결하고 2건의 대안을 제안하기로 의결하였습니다. 의결 법률안에 대한 심사 결과를 보고드리겠습니다. 먼저 국어기본법 일부개정법률안(대안)은 임오경·조계원 의원이 각각 대표발의한 2건의 법률안을 통합 조정한 것으로 현재 운영 중이나 법적 근거가 미비한 국어문화원연합회와 세종 한국어 평가의 법적 근거를 마련하는 내용입니다. 다음, 김승수 의원이 대표발의한 문화산업진흥 기본법 일부개정법률안은 한국콘텐츠진흥원의 문화상품 제작 지원 등을 위한 대출계정을 설치하여 장기간 지속된 융자사업의법적 근거를 마련하는 것으로 원안대로 의결하였습니다. 다음, 정연욱 의원이 대표발의한 이스포츠(전자스포츠) 진흥에 관한 법률 일부개정법률안은 지방자치단체의 지원 대상에 이스포츠팀의 창단 및 운영과 학교 및 청소년 대상이스포츠 활동과 진로교육 프로그램의 운영을 추가하려는 것으로 원안대로 의결하였습니다.",
    "전문위원입니다. 문화체육관광부 2차관 소관 총 6건의 법률안에 대한 검토의견을 간략히 요약해서 보고드리겠습니다. 1쪽 하단입니다. 의사일정 제28항 민형배 의원이 대표발의한 국민체육진흥법 일부개정법률안은 장애인올림픽대회라는 명칭을 국제적으로 통용되는 패럴림픽대회로 정비하고 국민체육진흥기금의 사용처와 서울올림픽기념국민체육진흥공단의 사업 범위에 서울패럴림픽 기념사업을명시하는 내용입니다. 장애인올림픽대회는 국제패럴림픽위원회가 주최하는 대회로 1989년 위원회가 설립된이후 패럴림픽이라는 용어로 사용되고 있다는 점에서 용어정비는 타당성이 있다고 보았습니다. 다만 서울올림픽기념국민체육진흥공단이 서울패럴림픽대회 기념사업도 담당하게 될경우 올림픽 기념만을 명시하고 있는 공단의 공식 명칭 및 목적도 변경될 필요가 있다고보았습니다. 3쪽입니다. 다음, 의사일정 제30항 임오경 의원이 대표발의한 문화관광축제 육성 및 지원에 관한법률안은 문화관광축제를 국가 관광경쟁력 제고와 지역발전의 전략적 플랫폼으로 육성하기 위하여 문화관광축제와 글로벌 축제의 지정 근거를 마련하고 문화관광축제 기본계획및 시행계획의 수립, 실태조사, 전문인력 양성, 전담 조직의 설치, 후원 및 기부금품의접수 등 행정적·재정적 지원체계를 구축하고자 하는 법안입니다. 동 법안은 축제 정책의 공공성·지속가능성을 강화하고 문화관광축제의 발전에 기여할것으로 기대되나 지역축제의 정의와 범위, 문화관광축제 전담 조직의 기부금품 접수조항 등에 대해서는 추가적인 검토가 필요할 것으로 보았습니다. 이하 내용은 생략하도록 하겠습니다. 감사합니다.",
    "79페이지를 보게 되면 수정의견의 24조의2 1항에 대한 의견입니다. 79페이지 당구장 표시에 ‘의무·재량여부 논의 필요’라고 돼 있는데요. 보통의 경우에 그 법령에서의무규정으로두는경우에는의무규정이후에의무를이행하지않을때벌칙규정을 두게 됩니다. 그런데 이것은 지금 산업통상부장관에게 어떠한 의무를 부여하는 것이라서 만약에 이렇게 의무를 부여했음에도 불구하고 이 법의 취지에 맞게 충분한 의무 이행을 하지 않는다고 나중에 추후에 판단을 하게 되면 나중에 산자부장관이 책임을 질 가능성이 좀 있어요. 그 점도 고려를 해서 입법을 하시는 게 좋을 것 같습니다. 그렇지는 않아요?",
    "검토의견과 수정의견에 대해서 동의합니다."
]

# ===============================
# 5️⃣ 실험 파라미터
# ===============================
ngram_ranges = [(1, 1), (1, 2)]
diversities = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
top_n = 5

# ===============================
# 6️⃣ 키워드 추출 실행
# ===============================
results = []
print("🚀 키워드 추출 실험 시작...")

with torch.no_grad():
    for doc_idx, doc in enumerate(test_docs):
        for nr in ngram_ranges:
            vectorizer = CountVectorizer(
                tokenizer=kiwi_tokenizer,
                ngram_range=nr,
                token_pattern=None
            )

            for div in diversities:
                try:
                    keywords = kw_model.extract_keywords(
                        docs=doc,
                        vectorizer=vectorizer,
                        use_mmr=True,
                        diversity=div,
                        top_n=top_n
                    )
                except Exception:
                    keywords = []

                results.append({
                    "doc_id": doc_idx + 1,
                    "ngram_range": nr,
                    "diversity": div,
                    "keywords": ", ".join([f"{k}({s:.2f})" for k, s in keywords])
                })

# ===============================
# 7️⃣ 결과 출력
# ===============================
df = pd.DataFrame(results)
pd.set_option("display.max_colwidth", None)

for i in range(len(test_docs)):
    print(f"\n--- [문서 {i+1}번 실험 결과] ---")
    sub_df = df[df["doc_id"] == i + 1][["ngram_range", "diversity", "keywords"]]
    print(sub_df.to_string(index=False))
