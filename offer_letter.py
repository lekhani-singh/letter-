import tkinter as tk
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def generate():
    name = e1.get()
    company = e2.get()
    position = e3.get()
    salary = e4.get()
    joining = e5.get()
    address = e6.get()
    email = e7.get()
    hr = e8.get()

    if not all([name, company, position, salary, joining, address, email, hr]):
        messagebox.showwarning("Error", "Please fill all details")
        return

    pdf = canvas.Canvas(name + "_offer_letter.pdf", pagesize=A4)
    w, h = A4

    navy = "#172A3A"
    gold = "#B4975A"
    cream = "#F8F5EF"

    # Background
    pdf.setFillColor(cream)
    pdf.rect(0, 0, w, h, fill=1)

    # Border
    pdf.setStrokeColor(gold)
    pdf.setLineWidth(2)
    pdf.rect(20, 20, w-40, h-40)

    # Company header
    pdf.setFillColor(navy)
    pdf.setFont("Helvetica-Bold", 21)
    pdf.drawString(65, h-70, company.upper())

    pdf.setFont("Helvetica", 8)
    pdf.drawString(65, h-85, "INNOVATION  •  DIGITAL  •  TOMORROW")

    # Address + email
    pdf.setFont("Helvetica", 8.5)
    pdf.drawRightString(w-65, h-65, address)
    pdf.drawRightString(w-65, h-80, email)

    # Header line
    pdf.setStrokeColor(gold)
    pdf.line(55, h-105, w-55, h-105)

    # Title
    pdf.setFillColor(navy)
    pdf.setFont("Helvetica-Bold", 22)
    pdf.drawCentredString(w/2, h-145, "OFFER LETTER")

    # Date
    pdf.setFont("Helvetica", 9)
    pdf.drawRightString(w-65, h-175, "Date: 06 September 2026")

    # Greeting
    pdf.setFont("Helvetica-Bold", 10.5)
    pdf.drawString(65, h-210, "Dear " + name + ",")

    # Main letter
    pdf.setFont("Helvetica", 10)

    lines = [
        f"We are pleased to offer you the position of {position}",
        f"at {company}.",
        "",
        f"Your annual salary will be Rs. {salary} per annum.",
        f"Your joining date will be {joining}.",
        "",
        "We look forward to welcoming you to our organization",
        "and wish you success in your professional journey."
    ]

    y = h - 235

    for line in lines:
        pdf.drawString(65, y, line)
        y -= 17

    # Offer details box
    y -= 5

    pdf.setFillColorRGB(1, 1, 1)
    pdf.setStrokeColor(gold)
    pdf.roundRect(65, y-105, w-130, 105, 7, fill=1)

    pdf.setFillColor(navy)
    pdf.setFont("Helvetica-Bold", 11)
    pdf.drawString(82, y-22, "OFFER DETAILS")

    details = [
        ("Position", position),
        ("Annual Salary", "Rs. " + salary),
        ("Joining Date", joining),
        ("Work Location", address)
    ]

    yy = y - 43
    pdf.setFont("Helvetica", 9)

    for label, value in details:
        pdf.setFont("Helvetica-Bold", 9)
        pdf.drawString(82, yy, label)
        pdf.drawString(165, yy, ":")
        pdf.setFont("Helvetica", 9)
        pdf.drawString(178, yy, value)
        yy -= 17

    # Signature
    pdf.setFillColor(navy)
    pdf.setFont("Helvetica", 10)
    pdf.drawString(65, y-140, "Best Regards,")

    # Signature line
    pdf.line(65, y-178, 160, y-178)

    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawString(65, y-195, hr)

    pdf.setFont("Helvetica", 9)
    pdf.drawString(65, y-210, "HR Manager")
    pdf.drawString(65, y-225, company)

    # Footer
    pdf.setStrokeColor(gold)
    pdf.line(65, 65, w-65, 65)

    pdf.setFont("Helvetica", 8)
    pdf.drawString(65, 48, address)
    pdf.drawRightString(w-65, 48, email)

    # Sample notice
    pdf.setFont("Helvetica-Oblique", 6.5)
    pdf.drawCentredString(w/2, 30, "SAMPLE / DEMO DOCUMENT")

    pdf.save()

    messagebox.showinfo("Success", "Offer Letter Created Successfully!")


# ---------------- APP ----------------

root = tk.Tk()
root.title("Offer Letter Generator")
root.geometry("500x680")
root.configure(bg="#F2EEE7")

tk.Label(
    root,
    text="OFFER LETTER GENERATOR",
    font=("Georgia", 19, "bold"),
    bg="#172A3A",
    fg="white",
    pady=15
).pack(fill="x")

fields = [
    "Employee Name",
    "Company Name",
    "Job Position",
    "Annual Salary",
    "Joining Date",
    "Company Address",
    "Company Gmail",
    "HR / Signature Name"
]

entries = []

for field in fields:
    tk.Label(
        root,
        text=field,
        bg="#F2EEE7",
        font=("Arial", 10, "bold")
    ).pack(pady=(7, 1))

    entry = tk.Entry(root, width=45)
    entry.pack(ipady=4)
    entries.append(entry)

e1, e2, e3, e4, e5, e6, e7, e8 = entries

tk.Button(
    root,
    text="GENERATE OFFER LETTER",
    command=generate,
    bg="#172A3A",
    fg="white",
    font=("Georgia", 11, "bold"),
    padx=20,
    pady=10
).pack(pady=20)

root.mainloop()