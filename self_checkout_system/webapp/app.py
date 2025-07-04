# webapp/app.py

import streamlit as st
import cv2
import pandas as pd

from config import LANGUAGES
from services.detection_service import DetectionService
from services.pricing_service import PricingService
from services.tts_service import TTSService

# —— 侧边栏语言选择 ——
st.sidebar.title("🌐 语言 / Language")
lang = st.sidebar.radio("", list(LANGUAGES.keys()), index=0)
ui = LANGUAGES[lang]

# —— 侧边栏身份选择 ——
st.sidebar.title(ui["ROLE_TITLE"])
role = st.sidebar.radio(ui["ROLE_LABEL"], ["Admin", "Customer"], index=0)

# —— 加载与初始化服务 ——
detector = DetectionService()
pricing  = PricingService(detector.model.names.values(), role)
tts      = TTSService(ui["TTS_LANG_CODE"])

# —— 价格输入 ——  
st.sidebar.title(ui["PRICE_TITLE"])
price_dict = pricing.get_price_dict()

# —— 主界面 ——  
st.title(ui["MAIN_TITLE"])

if st.button(ui["DETECT_BUTTON"]):
    try:
        frame = detector.capture_frame()
    except RuntimeError:
        st.error(ui["ERROR_CAMERA"])
    else:
        boxes, cls_ids, confs = detector.detect(frame)
        # 统计
        counts, total = {}, 0.0
        for cid in cls_ids:
            name = detector.model.names[cid]
            if name == "person": continue
            counts[name] = counts.get(name, 0) + 1

        rows = []
        for name, cnt in counts.items():
            unit = price_dict.get(name, 0.0)
            sub = round(cnt * unit, 2)
            total += sub
            rows.append({
                "Category": name, "Count": cnt,
                "Unit Price (RM)": unit, "Subtotal (RM)": sub
            })
        df = pd.DataFrame(rows)

        # 画框并展示
        for (x1, y1, x2, y2), cid, conf in zip(boxes, cls_ids, confs):
            cls_name = detector.model.names[cid]
            if cls_name == "person": continue
            cv2.rectangle(frame, (int(x1),int(y1)), (int(x2),int(y2)), (255,0,0), 2)
            cv2.putText(frame, f"{cls_name} {conf:.2f}",
                        (int(x1),int(y1)-5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1)

        st.table(df)
        st.image(frame, caption=ui["IMAGE_CAPTION"], use_container_width=True)
        st.markdown(ui["TOTAL_TEMPLATE"].format(total=total))

        # TTS 播报
        if counts:
            if lang == "English":
                parts = [f"{r['Category']} x{r['Count']}, unit price RM{r['Unit Price (RM)']}, subtotal RM{r['Subtotal (RM)']}" for r in rows]
                text = "; ".join(parts) + f"; total RM{round(total,2)}."
            else:
                parts = [f"{r['Category']} {r['Count']}个，单价RM{r['Unit Price (RM)']}，小计RM{r['Subtotal (RM)']}令吉" for r in rows]
                text = "；".join(parts) + f"；总计RM{round(total,2)}令吉。"
        else:
            text = ui["NO_ITEM_TEXT"]

        st.markdown(tts.speak(text), unsafe_allow_html=True)
