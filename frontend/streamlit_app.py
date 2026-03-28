import streamlit as st
import requests

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="LifeOS AI - Agent",
    page_icon="📬",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #0f172a, #1e293b);
            color: white;
        }
        .title {
            font-size: 42px;
            font-weight: 800;
            color: #38bdf8;
            text-align: center;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #cbd5e1;
            margin-bottom: 30px;
        }
        .card {
            background: #1e293b;
            padding: 20px;
            border-radius: 16px;
            margin-bottom: 20px;
            box-shadow: 0px 4px 20px rgba(0,0,0,0.25);
        }
        .success-box {
            background: #052e16;
            padding: 15px;
            border-radius: 12px;
            color: #86efac;
            font-weight: 600;
            margin-bottom: 20px;
        }
        .info-box {
            background: #082f49;
            padding: 15px;
            border-radius: 12px;
            color: #7dd3fc;
            font-weight: 500;
            margin-bottom: 15px;
        }
        .email-box {
            background: #334155;
            padding: 12px;
            border-radius: 10px;
            margin-bottom: 10px;
        }
        .summary-box {
            background: #1d4ed8;
            padding: 18px;
            border-radius: 14px;
            color: white;
            font-size: 17px;
            font-weight: 500;
            margin-bottom: 20px;
        }
        .badge-important {
            display: inline-block;
            background: #166534;
            color: #bbf7d0;
            padding: 4px 10px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: 700;
            margin-top: 6px;
        }
        .badge-newsletter {
            display: inline-block;
            background: #854d0e;
            color: #fde68a;
            padding: 4px 10px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: 700;
            margin-top: 6px;
        }
        .badge-promotional {
            display: inline-block;
            background: #7f1d1d;
            color: #fecaca;
            padding: 4px 10px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: 700;
            margin-top: 6px;
        }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown('<div class="title">📬 LifeOS Email Agent</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Clean inbox • Unsubscribe newsletters • Summarize important emails</div>',
    unsafe_allow_html=True
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("⚡ Quick Requests")
sample_requests = [
    "Clean my inbox",
    "Unsubscribe me from newsletters",
    "Give me a summary of my inbox",
    "Clean my inbox, unsubscribe newsletters, and summarize important emails"
]

selected_sample = st.sidebar.selectbox("Choose a sample request", [""] + sample_requests)

# -----------------------------
# Input
# -----------------------------
default_text = selected_sample if selected_sample else ""
user_request = st.text_area(
    "Enter your request",
    value=default_text,
    height=120,
    placeholder="Example: Clean my inbox and unsubscribe newsletters"
)

# -----------------------------
# API URL
# -----------------------------
API_URL = "http://127.0.0.1:8000/run"


# -----------------------------
# Helper: classification badge
# -----------------------------
def get_badge_html(classification: str):
    if classification == "important":
        return '<div class="badge-important">🟢 IMPORTANT</div>'
    elif classification == "newsletter":
        return '<div class="badge-newsletter">🟡 NEWSLETTER</div>'
    elif classification == "promotional":
        return '<div class="badge-promotional">🔴 PROMOTIONAL</div>'
    return ""


# -----------------------------
# Run Button
# -----------------------------
if st.button("🚀 Run Agent", use_container_width=True):
    if not user_request.strip():
        st.warning("Please enter a request.")
    else:
        with st.spinner("Running LifeOS agents..."):
            try:
                response = requests.post(
                    API_URL,
                    json={"user_request": user_request},
                    timeout=30
                )

                if response.status_code != 200:
                    st.error(f"Backend error: {response.text}")
                else:
                    data = response.json()

                    if data.get("status") == "success":
                        st.markdown(
                            '<div class="success-box">✅ Your request was processed successfully!</div>',
                            unsafe_allow_html=True
                        )

                        plan = data.get("plan", {})
                        intent_result = data.get("intent_result", {})
                        result = data.get("result", {})

                        # -----------------------------
                        # Human-readable main output
                        # -----------------------------
                        st.subheader("🤖 Agent Response")

                        action = result.get("action", "Action")
                        message = result.get("message", "Task completed.")

                        st.markdown(
                            f'<div class="summary-box"><b>{action}</b><br>{message}</div>',
                            unsafe_allow_html=True
                        )

                        # -----------------------------
                        # Planning + Intent
                        # -----------------------------
                        col1, col2 = st.columns(2)

                        with col1:
                            st.markdown('<div class="card">', unsafe_allow_html=True)
                            st.subheader("🧠 Planning")
                            st.write(f"**Domain:** {plan.get('domain', 'N/A')}")
                            st.write(f"**Intent:** {plan.get('intent', 'N/A')}")
                            st.write(f"**Why:** {plan.get('reason', 'N/A')}")
                            st.markdown('</div>', unsafe_allow_html=True)

                        with col2:
                            st.markdown('<div class="card">', unsafe_allow_html=True)
                            st.subheader("🎯 Intent Detection")
                            st.write(f"**Detected Intent:** {intent_result.get('intent', 'N/A')}")
                            st.write(f"**Reason:** {intent_result.get('reason', 'N/A')}")
                            st.markdown('</div>', unsafe_allow_html=True)

                        # -----------------------------
                        # Inbox Cleanup View
                        # -----------------------------
                        if action == "Inbox Cleanup":
                            st.markdown('<div class="card">', unsafe_allow_html=True)
                            st.subheader("🗑️ Cleanup Summary")
                            st.write(f"Found **{result.get('promotional_count', 0)} promotional emails** that can be cleaned.")
                            st.markdown('</div>', unsafe_allow_html=True)

                        # -----------------------------
                        # Unsubscribe View
                        # -----------------------------
                        unsubscribe_result = result.get("unsubscribe_result")
                        if unsubscribe_result:
                            st.markdown('<div class="card">', unsafe_allow_html=True)
                            st.subheader("📭 Newsletter Unsubscribe")
                            st.write(f"Processed **{unsubscribe_result.get('total_newsletters', 0)} newsletter emails**.")
                            for item in unsubscribe_result.get("unsubscribed_emails", []):
                                st.markdown(f"""
                                    <div class="email-box">
                                        ✅ Email ID <b>{item.get("id")}</b> → <b>{item.get("status")}</b><br>
                                        Reason: {item.get("reason")}
                                    </div>
                                """, unsafe_allow_html=True)
                            st.markdown('</div>', unsafe_allow_html=True)

                        # -----------------------------
                        # Summary View
                        # -----------------------------
                        summary_result = result.get("summary_result")
                        if summary_result:
                            st.markdown('<div class="card">', unsafe_allow_html=True)
                            st.subheader("📝 Inbox Summary")
                            st.markdown(
                                f'<div class="info-box">{summary_result.get("summary_text", "No summary available.")}</div>',
                                unsafe_allow_html=True
                            )
                            st.write(f"**Important Emails:** {summary_result.get('important_count', 0)}")
                            st.write(f"**Newsletters:** {summary_result.get('newsletter_count', 0)}")
                            st.write(f"**Promotional Emails:** {summary_result.get('promotional_count', 0)}")
                            st.markdown('</div>', unsafe_allow_html=True)

                        # -----------------------------
                        # Show Only Relevant / Changed Emails
                        # -----------------------------
                        with st.expander("📨 View Actioned / Important Emails"):
                            relevant_emails = []

                            # 1. Inbox Cleanup -> only promotional emails
                            if action == "Inbox Cleanup":
                                relevant_emails = result.get("promotional_emails", [])

                            # 2. Unsubscribe -> only unsubscribed newsletter emails
                            elif action == "Unsubscribe Newsletters":
                                unsubscribed_items = result.get("unsubscribe_result", {}).get("unsubscribed_emails", [])
                                all_emails = result.get("emails", [])

                                unsubscribed_ids = {item["id"] for item in unsubscribed_items}
                                relevant_emails = [email for email in all_emails if email["id"] in unsubscribed_ids]

                            # 3. Summary -> only important emails
                            elif action == "Generate Summary":
                                relevant_emails = result.get("summary_result", {}).get("important_emails", [])

                            # 4. Full Optimization -> promotional + unsubscribed + important
                            elif action == "Full Email Optimization":
                                all_emails = result.get("emails", [])

                                promotional = result.get("promotional_emails", [])
                                unsubscribed_items = result.get("unsubscribe_result", {}).get("unsubscribed_emails", [])
                                important = result.get("summary_result", {}).get("important_emails", [])

                                promotional_ids = {email["id"] for email in promotional}
                                unsubscribed_ids = {item["id"] for item in unsubscribed_items}
                                important_ids = {email["id"] for email in important}

                                combined_ids = promotional_ids.union(unsubscribed_ids).union(important_ids)
                                relevant_emails = [email for email in all_emails if email["id"] in combined_ids]

                            # Display relevant emails
                            if relevant_emails:
                                for email in relevant_emails:
                                    badge_html = get_badge_html(email.get("classification", ""))
                                    st.markdown(f"""
                                        <div class="email-box">
                                            <b>Email ID:</b> {email.get("id")} <br>
                                            <b>Classification:</b> {email.get("classification")} <br>
                                            <b>Reason:</b> {email.get("reason")} <br>
                                            {badge_html}
                                        </div>
                                    """, unsafe_allow_html=True)
                            else:
                                st.write("No relevant changed emails to display.")

                    else:
                        st.error("Agent returned an unexpected status.")
                        st.json(data)

            except requests.exceptions.ConnectionError:
                st.error("❌ Cannot connect to FastAPI backend. Make sure FastAPI is running on http://127.0.0.1:8000")
            except requests.exceptions.Timeout:
                st.error("⏳ Request timed out.")
            except Exception as e:
                st.error(f"Unexpected error: {str(e)}")