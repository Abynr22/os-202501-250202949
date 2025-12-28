def read_reference_string(filename):
    with open(filename, "r") as file:
        content = file.read()
        pages = list(map(int, content.replace(",", " ").split()))
    return pages


def fifo(pages, frames):
    memory = []
    faults = 0

    print("FIFO Simulation:")
    for page in pages:
        if page not in memory:
            faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
        print(f"Page {page} -> {memory}")

    print("Total Page Fault FIFO:", faults)


def lru(pages, frames):
    memory = []
    faults = 0

    print("\nLRU Simulation:")
    for page in pages:
        if page not in memory:
            faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
        else:
            memory.remove(page)
            memory.append(page)
        print(f"Page {page} -> {memory}")

    print("Total Page Fault LRU:", faults)


# ================= MAIN =================#
frames = 3  
pages = read_reference_string("reference_string.txt")

fifo(pages, frames)
lru(pages, frames)
