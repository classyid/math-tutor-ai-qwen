# Ubah import ini
from langchain_ollama import ChatOllama  # Import yang benar
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import time
import os

# Konfigurasi Model
OLLAMA_CONFIG = {
    "model": "qwen",
    "base_url": "http://<ip-server-Ollama>:11434",
    "temperature": 0.7,
    "top_k": 40,
    "top_p": 0.95,
    "num_ctx": 2048,
    "repeat_penalty": 1.1
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_with_typing(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def get_system_prompt() -> SystemMessage:
    return SystemMessage(content="""Kamu adalah asisten guru matematika yang sabar dan membantu.

Panduan mengajar:
1. Jelaskan konsep dengan sederhana dan mudah dipahami
2. Berikan langkah penyelesaian step by step
3. Sertakan contoh yang relevan
4. Jika siswa bingung, coba pendekatan penjelasan yang berbeda
5. Dorong siswa untuk berpikir kritis

Berikan jawaban dalam bahasa Indonesia yang jelas, singkat dan edukatif dengan contoh soal jika diperlukan.""")

def create_math_tutor():
    try:
        llm = ChatOllama(**OLLAMA_CONFIG)
        return llm
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    clear_screen()
    print("\n" + "="*50)
    print_with_typing("📚 Selamat datang di Asisten Belajar Matematika!")
    print_with_typing("🎓 Saya siap membantu kamu belajar matematika")
    print_with_typing("💡 Ketik 'keluar' untuk mengakhiri sesi belajar")
    print_with_typing("📝 Ketik 'clear' untuk membersihkan layar")
    print("="*50 + "\n")

    llm = create_math_tutor()
    if not llm:
        print_with_typing("❌ Gagal menginisialisasi asisten. Coba lagi nanti.")
        return

    messages = [get_system_prompt()]

    while True:
        try:
            user_input = input("\n👨‍🎓 Siswa: ")
            
            if user_input.lower() == 'keluar':
                print_with_typing("\n👨‍🏫 Guru: Semangat belajar! Sampai jumpa lagi! 👋")
                break
            elif user_input.lower() == 'clear':
                clear_screen()
                messages = [get_system_prompt()]
                continue
            elif not user_input.strip():
                continue

            print("\n👨‍🏫 Guru: ", end='', flush=True)
            
            messages.append(HumanMessage(content=user_input))
            response = llm.invoke(messages)
            messages.append(AIMessage(content=response.content))
            
            print_with_typing(response.content, delay=0.02)
            
        except KeyboardInterrupt:
            print_with_typing("\n\n👨‍🏫 Guru: Sesi belajar diinterupsi. Sampai jumpa! 👋")
            break
        except Exception as e:
            print(f"\n❌ Terjadi error: {e}")
            print("Silakan coba lagi.")

if __name__ == "__main__":
    main()
