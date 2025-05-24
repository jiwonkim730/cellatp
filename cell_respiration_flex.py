import streamlit as st

st.title("ATP 생성 계산기")

# 포도당 분자 수 입력
glucose_molecules = st.number_input("포도당 분자 수", min_value=1, value=1, step=1)

# 반복 횟수 입력
user_glycolysis = st.number_input("해당과정 반복 횟수", min_value=0, value=1, step=1)
user_pyruvate_oxidation = st.number_input("피루브산 산화 반복 횟수", min_value=0, value=2, step=1)
user_tca_cycles = st.number_input("TCA 회로 반복 횟수", min_value=0, value=2, step=1)

# 가능한 최대 횟수
max_glycolysis = glucose_molecules
max_pyruvate_oxidation = glucose_molecules * 2
max_tca_cycles = glucose_molecules * 2

# 경고 메시지
if user_glycolysis > max_glycolysis:
    st.warning(f"해당과정은 최대 {max_glycolysis}회까지만 유효. 계산은 {max_glycolysis}회로 제한됩니다.")
if user_pyruvate_oxidation > max_pyruvate_oxidation:
    st.warning(f"피루브산 산화는 최대 {max_pyruvate_oxidation}회까지만 유효. 계산은 {max_pyruvate_oxidation}회로 제한됩니다.")
if user_tca_cycles > max_tca_cycles:
    st.warning(f"TCA 회로는 최대 {max_tca_cycles}회까지만 유효. 계산은 {max_tca_cycles}회로 제한됩니다.")

# 실제 계산에 사용할 횟수
glycolysis_runs = min(user_glycolysis, max_glycolysis)
pyruvate_oxidations = min(user_pyruvate_oxidation, max_pyruvate_oxidation)
tca_cycles = min(user_tca_cycles, max_tca_cycles)

# 해당과정
glycolysis_atp = 2 * glycolysis_runs
glycolysis_nadh = 2 * glycolysis_runs

# 피루브산 산화
pyruvate_nadh = 1 * pyruvate_oxidations

# TCA 회로
tca_atp = 1 * tca_cycles
tca_nadh = 3 * tca_cycles
tca_fadh2 = 1 * tca_cycles

# 산화적 인산화
atp_per_nadh = 2.5
atp_per_fadh2 = 1.5
oxidative_atp = (glycolysis_nadh + pyruvate_nadh + tca_nadh) * atp_per_nadh + tca_fadh2 * atp_per_fadh2

# 총 ATP
total_atp = glycolysis_atp + tca_atp + oxidative_atp

# 출력
st.subheader("계산 결과")
st.write(f"해당과정: ATP {glycolysis_atp}개, NADH {glycolysis_nadh}개")
st.write(f"피루브산 산화: NADH {pyruvate_nadh}개")
st.write(f"TCA 회로: ATP {tca_atp}개, NADH {tca_nadh}개, FADH2 {tca_fadh2}개")
st.write(f"산화적 인산화: {(glycolysis_nadh + pyruvate_nadh + tca_nadh)} NADH × 2.5 + {tca_fadh2} FADH2 × 1.5 = {oxidative_atp:.1f} ATP")
st.markdown(f"### 🧪 총 ATP 생성량: {total_atp:.1f} 개")
