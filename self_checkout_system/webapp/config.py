# webapp/config.py

# --- 语言与界面文案 ---
LANGUAGES = {
    "English": {
        "ROLE_TITLE":        "🔑 Role Selection",
        "ROLE_LABEL":        "Current Role:",
        "PRICE_TITLE":       "🛒 Product Prices (RM)",
        "MAIN_TITLE":        "Self-Service Checkout System",
        "DETECT_BUTTON":     "Start Detection and Checkout",
        "ERROR_CAMERA":      "Failed to read from the camera. Please check your device and permissions.",
        "IMAGE_CAPTION":     "Detection Result",
        "TOTAL_TEMPLATE":    "### Total: **RM {total:.2f}**",
        "NO_ITEM_TEXT":      "No items detected.",
        "TTS_LANG_CODE":     "en",
    },
    "中文": {
        "ROLE_TITLE":        "🔑 身份选择",
        "ROLE_LABEL":        "当前身份：",
        "PRICE_TITLE":       "🛒 商品价格 (RM)",
        "MAIN_TITLE":        "无人自助结账系统",
        "DETECT_BUTTON":     "开始检测并报价",
        "ERROR_CAMERA":      "无法读取摄像头，请检查设备和权限。",
        "IMAGE_CAPTION":     "检测结果",
        "TOTAL_TEMPLATE":    "### 总计：**RM {total:.2f}**",
        "NO_ITEM_TEXT":      "未检测到商品。",
        "TTS_LANG_CODE":     "zh-cn",
    },
}
