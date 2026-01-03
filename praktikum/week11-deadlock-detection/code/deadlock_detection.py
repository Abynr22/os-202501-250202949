import csv
import os

def print_table(data):
    if not data:
        print("[!] Tabel Kosong. Periksa format CSV Anda.")
        return
    
    headers = ["Process", "Allocation", "Request"]
    col_width = 12
    
    line = "+" + ("-" * (col_width + 2) + "+") * len(headers)
    print(line)
    print("| " + " | ".join(h.ljust(col_width) for h in headers) + " |")
    print(line)
    
    for row in data:
        print("| " + " | ".join(row.get(h, "").ljust(col_width) for h in headers) + " |")
    print(line)

def detect_deadlock(file_path):
    adj = {}
    raw_data = []
    
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} tidak ditemukan.")
        return

    try:
        # Menggunakan utf-8-sig untuk membuang karakter aneh di awal file
        with open(file_path, mode='r', encoding='utf-8-sig') as file:
            # Membaca mentah dulu untuk deteksi delimiter
            content = file.read()
            dialect = csv.Sniffer().sniff(content)
            file.seek(0)
            
            # Membaca CSV
            reader = csv.DictReader(file, delimiter=dialect.delimiter)
            
            # NORMALISASI: Bersihkan spasi dari nama kolom (header)
            reader.fieldnames = [name.strip() for name in reader.fieldnames]
            
            for row in reader:
                # NORMALISASI: Bersihkan spasi dari setiap nilai di dalam sel
                p = row.get('Process', '').strip()
                alloc = row.get('Allocation', '').strip()
                req = row.get('Request', '').strip()
                
                if p and alloc and req:
                    raw_data.append({'Process': p, 'Allocation': alloc, 'Request': req})
                    
                    # RAG: Resource -> Process (Holding)
                    if alloc not in adj: adj[alloc] = []
                    adj[alloc].append(p)
                    
                    # RAG: Process -> Resource (Requesting)
                    if p not in adj: adj[p] = []
                    adj[p].append(req)
                
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return

    print("\n--- DATASET DEADLOCK ---")
    print_table(raw_data)

    # Algoritma DFS untuk mencari Cycle
    visited = set()
    rec_stack = []

    def find_cycle(v):
        visited.add(v)
        rec_stack.append(v)
        
        for neighbor in adj.get(v, []):
            if neighbor not in visited:
                if find_cycle(neighbor): return True
            elif neighbor in rec_stack:
                start_idx = rec_stack.index(neighbor)
                cycle = rec_stack[start_idx:]
                print("\n[!] STATUS: TERDETEKSI DEADLOCK!")
                print(f"[!] Jalur Siklus: {' -> '.join(cycle)} -> {neighbor}")
                return True
        
        rec_stack.pop()
        return False

    print("\n--- Menganalisis Resource Allocation Graph ---")
    found = False
    for node in list(adj.keys()):
        if node not in visited:
            if find_cycle(node):
                found = True
                break
    
    if not found:
        print("\n[V] STATUS: AMAN (Sistem bebas dari deadlock)")

if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    csv_path = os.path.join(current_dir, "dataset_deadlock.csv")
    detect_deadlock(csv_path)