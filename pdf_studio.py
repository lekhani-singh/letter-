import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter


# ---------- FUNCTIONS ----------

def merge_pdf():
    files = filedialog.askopenfilenames(
        title="Select PDF Files",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if len(files) < 2:
        messagebox.showwarning("Oops!", "Please select at least 2 PDFs.")
        return

    save = filedialog.asksaveasfilename(
        title="Save Merged PDF",
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if not save:
        return

    writer = PdfWriter()

    for file in files:
        reader = PdfReader(file)
        for page in reader.pages:
            writer.add_page(page)

    with open(save, "wb") as f:
        writer.write(f)

    messagebox.showinfo("Success ✨", "Your PDFs are merged!")


def split_pdf():
    file = filedialog.askopenfilename(
        title="Select PDF",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if not file:
        return

    folder = filedialog.askdirectory(
        title="Choose Output Folder"
    )

    if not folder:
        return

    reader = PdfReader(file)

    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)

        with open(f"{folder}/Page_{i+1}.pdf", "wb") as f:
            writer.write(f)

    messagebox.showinfo(
        "Done ✨",
        f"PDF split into {len(reader.pages)} pages!"
    )


# ---------- MAIN WINDOW ----------

root = tk.Tk()
root.title("PDF Studio ♡")
root.geometry("520x520")
root.resizable(False, False)
root.configure(bg="#FFF8F2")


# ---------- HEADER ----------

header = tk.Frame(
    root,
    bg="#5B4B8A",
    height=130
)
header.pack(fill="x")


tk.Label(
    header,
    text="📄  PDF STUDIO",
    font=("Georgia", 27, "bold"),
    bg="#5B4B8A",
    fg="white"
).pack(pady=(25, 5))


tk.Label(
    header,
    text="Simple • Cute • Easy PDF Tools",
    font=("Arial", 11),
    bg="#5B4B8A",
    fg="#EDE7F6"
).pack()


# ---------- WELCOME ----------

tk.Label(
    root,
    text="What would you like to do? ✨",
    font=("Georgia", 16, "bold"),
    bg="#FFF8F2",
    fg="#3F365C"
).pack(pady=(30, 20))


# ---------- BUTTONS ----------

tk.Button(
    root,
    text="📑   Merge PDFs",
    command=merge_pdf,
    font=("Arial", 13, "bold"),
    bg="#8E7CC3",
    fg="white",
    activebackground="#7565A5",
    relief="flat",
    width=25,
    height=2,
    cursor="hand2"
).pack(pady=10)


tk.Button(
    root,
    text="✂   Split PDF",
    command=split_pdf,
    font=("Arial", 13, "bold"),
    bg="#D88C9A",
    fg="white",
    activebackground="#C57483",
    relief="flat",
    width=25,
    height=2,
    cursor="hand2"
).pack(pady=10)


tk.Button(
    root,
    text="❌   Exit",
    command=root.destroy,
    font=("Arial", 11),
    bg="#6D6875",
    fg="white",
    relief="flat",
    width=18,
    cursor="hand2"
).pack(pady=20)


# ---------- FOOTER ----------

tk.Label(
    root,
    text="♡ Made with Python & Tkinter ♡",
    font=("Arial", 10),
    bg="#FFF8F2",
    fg="#8A7F8D"
).pack(pady=(10, 3))


tk.Label(
    root,
    font=("Georgia", 11, "bold"),
    bg="#FFF8F2",
    fg="#5B4B8A"
).pack()


root.mainloop()