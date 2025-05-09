import streamlit as st
import pandas as pd

quiz_data = [
    {"question": "蜈蚣和马陆有什么不同？", "options": ["蜈蚣是扁的，马陆是圆的", "马陆会咬人，蜈蚣不会", "马陆腿比较少", "它们其实一样"], "answer": "蜈蚣是扁的，马陆是圆的"},
    {"question": "章鱼有几个心脏？", "options": ["一个", "两个", "三个", "八个"], "answer": "三个"},
    {"question": "身体哪个部位没有血管？", "options": ["舌头", "皮肤", "角膜", "耳朵"], "answer": "角膜"},
    {"question": "瑞士的首都是哪？", "options": ["苏黎世", "伯尔尼", "日内瓦", "洛桑"], "answer": "伯尔尼"},
    {"question": "哪种金属在室温下是液体？", "options": ["汞", "铅", "锌", "铝"], "answer": "汞"},
    {"question": "金星的一天有多长？", "options": ["24小时", "7天", "117地球日", "一地球年"], "answer": "117地球日"},
    {"question": "太阳从哪个方向升起？", "options": ["北方", "南方", "东方", "西方"], "answer": "东方"},
    {"question": "哪种动物不会跳？", "options": ["袋鼠", "大象", "青蛙", "猫"], "answer": "大象"},
    {"question": "水在海平面下的沸点是多少？", "options": ["90°C", "95°C", "100°C", "105°C"], "answer": "100°C"},
    {"question": "哪个行星离太阳最近？", "options": ["地球", "火星", "水星", "金星"], "answer": "水星"},
    {"question": "人体中最大的器官是什么？", "options": ["肝脏", "肺", "脑", "皮肤"], "answer": "皮肤"},
    {"question": "黄金会生锈吗？", "options": ["会", "不会", "只有在水里才会", "只有遇到空气才会"], "answer": "不会"},
    {"question": "鱼会睡觉吗？", "options": ["不会", "会", "只在冬天睡", "只在黑暗中睡"], "answer": "会"},
    {"question": "长颈鹿的舌头是什么颜色？", "options": ["红色", "黑色", "粉色", "蓝色"], "answer": "黑色"},
    {"question": "哪种语言的母语人数最多？", "options": ["英语", "印地语", "西班牙语", "中文"], "answer": "中文"}
]

if "score" not in st.session_state:
    st.session_state.score = 0
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "completed" not in st.session_state:
    st.session_state.completed = False
if "history" not in st.session_state:
    st.session_state.history = []


st.set_page_config(page_title="这些知识真的是‘常识’吗？", page_icon="🧠", layout="centered")
st.markdown("<h1 style='text-align: center; color: #2E86AB;'>🧠 这些知识真的是‘常识’吗？</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>一个关于“常识”的小测验，灵感来自《二、沙上有印，风中有音，光中有影》中的《常识》。</p>", unsafe_allow_html=True)
st.markdown("<hr style='border-top: 3px solid #bbb;'>", unsafe_allow_html=True)


if not st.session_state.completed:
    q = quiz_data[st.session_state.q_index]
    st.subheader(f"📍 第 {st.session_state.q_index + 1} 题")
    st.markdown(f"**{q['question']}**")

    choice = st.radio("请选择你的答案：", q["options"], key=f"choice_{st.session_state.q_index}")

    if st.button("✅ 提交答案"):
        correct = choice == q["answer"]
        if correct:
            st.success("太棒了，回答正确！🎉")
            st.session_state.score += 1
        else:
            st.warning("这个问题答错啦，不过继续加油！")

        st.session_state.history.append({
            "题目": q["question"],
            "你的回答": choice,
            "是否正确": "✔️" if correct else "❌"
        })

        if st.session_state.q_index + 1 < len(quiz_data):
            st.session_state.q_index += 1
        else:
            st.session_state.completed = True
        st.rerun()

else:
    st.balloons()
    st.success(f"🎯 你完成了测验！最终得分：**{st.session_state.score} / {len(quiz_data)}**")

    correct_df = pd.DataFrame([item for item in st.session_state.history if item["是否正确"] == "✔️"])
    if not correct_df.empty:
        st.markdown("### ✅ 你答对了这些题：")
        st.dataframe(correct_df[["题目", "你的回答"]], use_container_width=True)
    else:
        st.info("你目前还没有答对任何题，建议再试一次！")

    st.markdown("### 📘 项目说明")
    st.info("""
这个小测验的灵感来自《常识》这篇文章。在文中，作者因为不认识“马陆”而感到尴尬，也让我们意识到：所谓“常识”并不总是人人都知道。
透过这 15 个问题，你可能也发现了一些从没认真想过的事情。这不仅是测验，更是一次对日常知识的重新审视。
    """)

    if st.button("🔁 再玩一次"):
        st.session_state.score = 0
        st.session_state.q_index = 0
        st.session_state.completed = False
        st.session_state.history = []
        st.rerun()