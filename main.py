import heapq
import pickle

# =========================
# Job Class
# =========================
class Job:
    def __init__(self, job_id, job_name, priority, exec_time):
        self.job_id = job_id
        self.job_name = job_name
        self.priority = priority
        self.exec_time = exec_time

    def __str__(self):
        return f"ID:{self.job_id}, Name:{self.job_name}, Priority:{self.priority}, Time:{self.exec_time}"


# =========================
# Data Structures
# =========================
job_queue = []          # Queue (FCFS)
priority_heap = []     # Heap (Priority Queue)
job_bst = {}            # BST (dictionary used for simplicity)


# =========================
# Insert Job
# =========================
def insert_job():
    job_id = int(input("Enter Job ID: "))
    if job_id in job_bst:
     print("❌ Job ID already exists.")
     return
    job_name = input("Enter Job Name: ")
    priority = int(input("Enter Priority (1 = High): "))
    exec_time = int(input("Enter Execution Time: "))

    job = Job(job_id, job_name, priority, exec_time)

    # Queue
    job_queue.append(job)

    # Heap (priority, job)
    heapq.heappush(priority_heap, (priority, job))

    # BST (using dictionary)
    job_bst[job_id] = job

    print("✅ Job inserted successfully!")


# =========================
# Search Job
# =========================
def search_job():
    job_id = int(input("Enter Job ID to search: "))
    if job_id in job_bst:
        print("✅ Job Found:")
        print(job_bst[job_id])
    else:
        print("❌ Job not found.")


# =========================
# Delete Job
# =========================
def delete_job():
    job_id = int(input("Enter Job ID to delete: "))
    if job_id in job_bst:
        del job_bst[job_id]
        print("✅ Job deleted from system.")
    else:
        print("❌ Job not found.")


# =========================
# Display Jobs
# =========================
def display_jobs():
    print("\n--- Queue (Arrival Order) ---")
    for job in job_queue:
        print(job)

    print("\n--- Priority Queue (Heap Order) ---")
    for item in priority_heap:
        print(item[1])

    print("\n--- BST (Sorted by Job ID) ---")
    for key in sorted(job_bst):
        print(job_bst[key])


# =========================
# File Handling
# =========================
def save_to_file():
    with open("jobs.dat", "wb") as file:
        pickle.dump(job_bst, file)
    print("💾 Data saved to file.")


def load_from_file():
    global job_bst
    try:
        with open("jobs.dat", "rb") as file:
            job_bst = pickle.load(file)
        print("📂 Data loaded from file.")
    except:
        print("❌ No file found.")


# =========================
# Menu
# =========================
def menu():
    while True:
        print("\n======================================")
        print("   SMART JOB SCHEDULER SYSTEM")
        print("======================================")
        print("1. Insert Job")
        print("2. Search Job")
        print("3. Delete Job")
        print("4. Display Jobs")
        print("5. Save to File")
        print("6. Load from File")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            insert_job()
        elif choice == '2':
            search_job()
        elif choice == '3':
            delete_job()
        elif choice == '4':
            display_jobs()
        elif choice == '5':
            save_to_file()
        elif choice == '6':
            load_from_file()
        elif choice == '7':
            print("👋 Thank you for using Smart Job Scheduler System!")
            break
        else:
            print("❌ Invalid choice")


# =========================
# Run Program
# =========================
menu()
