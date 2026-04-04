# 📁 Elasticsearch 노트

> Elasticsearch를 활용하여 검색 시스템의 구조, 성능, 확장성을 실험한 프로젝트 및 학습 노트

---

## 🧾 프로젝트 정보
- 프로젝트 형태: 개인 프로젝트(검색 시스템 설계 및 성능 실험)
- 개발 기간: 2025.11 ~ 2025.12
- 성적: A+ (최상위 성적) 취득
- 결과:
   - 단일 노드 vs 클러스터 환경 성능 비교 실험 수행
   - 검색 시스템의 확장성과 장애 대응 구조 검증
   - Elasticsearch 기반 검색 엔진 설계 및 구현 경험 확보

📗 **Notion 문서**  
- [미니 프로젝트 전체 설명 노션 페이지](https://www.notion.so/Elasticsearch-2a9809750eed8068958ef08144509628?source=copy_link)

📄 **PDF 문서**  
- [파이프라인 이해를 위한 문서](https://github.com/Hwang-Injun34/elasticsearch_notes/blob/main/%E1%84%91%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%91%E1%85%B3%E1%84%85%E1%85%A1%E1%84%8B%E1%85%B5%E1%86%AB%20%E1%84%8B%E1%85%B5%E1%84%92%E1%85%A2%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%8B%E1%85%B1%E1%84%92%E1%85%A1%E1%86%AB%20%E1%84%86%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5.pdf)
- [Politi-Search 통합 보고서](https://github.com/Hwang-Injun34/elasticsearch_notes/blob/main/Politi-Search_%E1%84%90%E1%85%A9%E1%86%BC%E1%84%92%E1%85%A1%E1%86%B8_%E1%84%87%E1%85%A9%E1%84%80%E1%85%A9%E1%84%89%E1%85%A5_%E1%84%82%E1%85%A1%E1%86%B7%E1%84%80%E1%85%AE%E1%86%BC%E1%84%86%E1%85%A7%E1%86%BC%E1%84%89%E1%85%AE.pdf)

▶️ **시연 영상**  
- [클라우드컴퓨팅 시연 영상](https://github.com/Hwang-Injun34/elasticsearch_notes/blob/main/%E1%84%8F%E1%85%B3%E1%86%AF%E1%84%85%E1%85%A1%E1%84%8B%E1%85%AE%E1%84%83%E1%85%B3%E1%84%8F%E1%85%A5%E1%86%B7%E1%84%91%E1%85%B2%E1%84%90%E1%85%B5%E1%86%BC%20%E1%84%89%E1%85%B5%E1%84%8B%E1%85%A7%E1%86%AB%20%E1%84%8B%E1%85%A7%E1%86%BC%E1%84%89%E1%85%A1%E1%86%BC.mov)

---

## 📌 프로젝트 개요
Elasticsearch의 내부 구조와 검색 동작 원리를 이해하고,<br>
단일 노드부터 클러스터 환경까지 확장하며<br>
검색 시스템의 설계 및 운영 방식을 실험하기 위해 진행된 프로젝트입니다.

단순 개념 학습을 넘어,<br>
실제 서비스 환경을 가정하여 확장성과 대응까지 고려한 시스템 구조를 설계 및 구현하였습니다.

또한 동일한 데이터셋과 애플리케이션 환경에서 <br>
시스템 구성 방식에 따른 성능 및 동작 차이를 분석하는 데 중점을 두었습니다.

---

## 🚨 문제 정의
기존 애플리케이션의 검색 기능은  
DB 기반 단순 쿼리에 의존하는 경우가 많아 다음과 같은 한계가 존재합니다.
- 대량 데이터에서 검색 성능 저하
- 복잡한 조건 검색 및 랭킹 처리의 어려움
- 시스템 확장성과 장애 대응 구조 부족  <br>

또한 검색 시스템을 설계할 때
단일 노드와 클러스터 구조 간의 차이와 트레이드오프를<br>
명확히 이해하기 어렵다는 문제가 있습니다.

---

## 💡 해결 전략
- Elasitcsearch 기반 검색 엔진 도입
- Inverted Index 기반 검색 구조 활용
- 단일 노드 → 클러스터 구조로 확장 실험
- Master / Data 노드 분리를 통한 역할 기반 설계
- Shard 기반 데이터 분산 처리 구조 적용
- 장애 상황 테스트 및 복구 과정 검증

---

## 📚 학습 내용

### Elasticsearch 개념
- Cluster / Node / Index / Shard 구조
- Inverted Index 기반 검색 원리
- 검색 쿼리 및 스코어링 방식

📗 **Notion 문서**  
- [Elasticsearch 개념 정리 노션 페이지](https://www.notion.so/2ab809750eed80c7bc22c71a7a8c1941?source=copy_link)

---
## 🏗 프로젝트 구성
### 1️⃣ 싱글 노드 Elasticsearch
- 단일 노드 환경에서 Elasticsearch 구성
- Docker 기반 실행
- CRUD 및 Search API 실습
- 인덱싱 및 기본 검색 동작 확인

🔗 **GitHub 저장소**  
- [single_node_elasticsearch_project](https://github.com/Hwang-Injun34/single_node_elasticsearch_project)


### 2️⃣ 클러스터 기반 Elasticsearch
- 다중 노드 클러스터 구성
- Master / Data 노드 분리
- Shard 기반 데이터 분산 처리
- 장애 상황 테스트 및 복구 실험

🔗 **GitHub 저장소**  
- [clustered_elasticsearch_project](https://github.com/Hwang-Injun34/clustered_elasticsearch_project)

---

## 📊 실험 내용
- 단일 노드 vs 클러스터 환경 성능 비교
- Shard 분산 방식에 따른 데이터 처리 구조 분석
- 인덱싱 속도 및 검색 응답 시간 비교
- 노드 장애 발생 시 복구 과정 및 데이터 안정성 확인

---

## 📊 결과 및 인사이트
- 클러스터 환경에서 데이터 분산 처리로 확장성 확보
- 단일 노드는 구조가 단순하지만 확장성에 한계 존재
- Shard 설계가 성능 및 안정성에 중요한 역할을 미침
- 장애 발생 시 Replica를 통한 데이터 복구 가능 확인

---
## 🛠 기술 스택

- Elasticsearch
- Docker / Docker Compose
- FastAPI
- Nginx

---

## 🗂 정리 방식
- ▶️ **시연 영상**: MP4
- 📄 **이론 & 개념, 보고서**: PDF
- 📗 **이론 & 개념**: Notion
- 🔗  **실습 & 코드**: GitHub

