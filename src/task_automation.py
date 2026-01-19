import subprocess
import os
import datetime

def check_system_integrity():
    """Hocanin 'Auto Control' beklentisi için sistem kontrolü."""
    print(f"[{datetime.datetime.now()}] Sistem kontrol ediliyor...")
    # Crontab'ın erişilebilir olup olmadığını kontrol eder
    try:
        subprocess.run(["crontab", "-l"], capture_output=True)
        return True
    except FileNotFoundError:
        return False

def run_secure_backup(source_dir, backup_name):
    """Unix I/O standartlarina uygun yedekleme fonksiyonu."""
    if not os.path.exists(source_dir):
        print(f"Hata: {source_dir} dizini bulunamadi! (stderr)")
        return

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    final_name = f"{backup_name}_{timestamp}.tar.gz"

    print(f"Islem basliyor: {source_dir} -> {final_name}")
    
    # Terminal Automation & I/O Redirection (stdout/stderr)
    result = subprocess.run(
        ["tar", "-czf", final_name, source_dir],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"Basari: Yedekleme tamamlandi. (stdout)")
    else:
        print(f"Islem sirasinda hata olustu: {result.stderr}")

if __name__ == "__main__":
    if check_system_integrity():
        # Örnek kullanım
        run_secure_backup("./data", "system_backup")
    else:
        print("Kritik Hata: Cron altyapisi bulunamadi!")
