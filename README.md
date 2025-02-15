# 🎓 Math Tutor AI - Asisten Matematika Pintar

Asisten belajar matematika berbasis AI yang dibangun menggunakan LangChain dan model Qwen. Dirancang untuk membantu siswa memahami konsep matematika dengan cara yang interaktif dan menyenangkan.

## ✨ Fitur
- 🤖 AI Responsif dengan model Qwen
- 📚 Penjelasan step-by-step yang mudah dipahami
- 🎯 Fokus pada pemahaman konsep
- 💡 Contoh soal interaktif
- 🔄 Memori percakapan untuk pembelajaran berkelanjutan
- 🖥️ Antarmuka konsol yang bersih dan mudah digunakan
- ⚡ Respon cepat dan efisien

## 🚀 Cara Penggunaan
1. Pastikan Python 3.x terinstal di sistem Anda
2. Install dependensi yang diperlukan:
   ```bash
   pip install langchain-ollama langchain-core
3. Pastikan server Ollama dengan model Qwen berjalan
4. Jalankan aplikasi:
   ```bash
   python app.py
   ```

## 🛠️ Konfigurasi
Anda dapat menyesuaikan parameter AI di file `app.py`:
```python
OLLAMA_CONFIG = {
    "model": "qwen",
    "temperature": 0.7,
    "top_k": 40,
    "top_p": 0.95
}
```

## 📋 Persyaratan Sistem
- Python 3.x
- Server Ollama dengan model Qwen
- Koneksi internet untuk akses server Ollama
- RAM minimal 4GB

## 🤝 Kontribusi
Kontribusi selalu disambut! Silakan buat pull request atau buka issue untuk saran dan perbaikan.

## 📝 Lisensi
MIT License
