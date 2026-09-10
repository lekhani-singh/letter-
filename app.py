import tkinter as tk
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors


def generate_certificate():

    name = name_entry.get().strip()
    workshop = workshop_entry.get().strip()
    college = college_entry.get().strip()
    date = date_entry.get().strip()
    signature = signature_entry.get().strip()

    if not name or not workshop or not college or not date or not signature:
        messagebox.showwarning(
            "Missing Information",
            "Please fill all the details."
        )
        return

    file_name = name.replace(" ", "_") + "_Certificate.pdf"

    # A4 LANDSCAPE
    width, height = landscape(A4)

    pdf = canvas.Canvas(file_name, pagesize=(width, height))

    # =========================================
    # BACKGROUND
    # =========================================

    pdf.setFillColor(colors.HexColor("#F8F5EC"))
    pdf.rect(0, 0, width, height, fill=1, stroke=0)

    # =========================================
    # OUTER BORDER
    # =========================================

    pdf.setStrokeColor(colors.HexColor("#17365D"))
    pdf.setLineWidth(5)
    pdf.rect(25, 25, width - 50, height - 50)

    # GOLD INNER BORDER
    pdf.setStrokeColor(colors.HexColor("#C49A3A"))
    pdf.setLineWidth(2)
    pdf.rect(40, 40, width - 80, height - 80)

    # =========================================
    # TOP DECORATION
    # =========================================

    pdf.setStrokeColor(colors.HexColor("#17365D"))
    pdf.setLineWidth(14)

    pdf.arc(
        width - 170,
        height - 110,
        width + 40,
        height + 50,
        0,
        90
    )

    pdf.setStrokeColor(colors.HexColor("#C49A3A"))
    pdf.setLineWidth(4)

    pdf.arc(
        width - 175,
        height - 115,
        width + 35,
        height + 45,
        0,
        90
    )

    # =========================================
    # BOTTOM LEFT DECORATION
    # =========================================

    pdf.setStrokeColor(colors.HexColor("#17365D"))
    pdf.setLineWidth(14)

    pdf.arc(
        -40,
        -40,
        170,
        120,
        180,
        90
    )

    pdf.setStrokeColor(colors.HexColor("#C49A3A"))
    pdf.setLineWidth(4)

    pdf.arc(
        -35,
        -35,
        165,
        115,
        180,
        90
    )

    # =========================================
    # COLLEGE NAME
    # =========================================

    pdf.setFillColor(colors.HexColor("#17365D"))
    pdf.setFont("Helvetica-Bold", 17)

    pdf.drawCentredString(
        width / 2,
        height - 82,
        college.upper()
    )

    # Gold line
    pdf.setStrokeColor(colors.HexColor("#C49A3A"))
    pdf.setLineWidth(2)

    pdf.line(
        230,
        height - 100,
        width - 230,
        height - 100
    )

    # =========================================
    # MAIN TITLE
    # =========================================

    pdf.setFillColor(colors.HexColor("#17365D"))
    pdf.setFont("Helvetica-Bold", 34)

    pdf.drawCentredString(
        width / 2,
        height - 150,
        "CERTIFICATE"
    )

    pdf.setFillColor(colors.HexColor("#C49A3A"))
    pdf.setFont("Helvetica-Bold", 18)

    pdf.drawCentredString(
        width / 2,
        height - 178,
        "OF PARTICIPATION"
    )

    # =========================================
    # PRESENTED TO
    # =========================================

    pdf.setFillColor(colors.HexColor("#333333"))
    pdf.setFont("Helvetica-Oblique", 14)

    pdf.drawCentredString(
        width / 2,
        height - 220,
        "This certificate is proudly presented to"
    )

    # =========================================
    # PARTICIPANT NAME
    # =========================================

    pdf.setFillColor(colors.HexColor("#17365D"))
    pdf.setFont("Helvetica-Bold", 27)

    pdf.drawCentredString(
        width / 2,
        height - 265,
        name
    )

    # Name underline
    pdf.setStrokeColor(colors.HexColor("#C49A3A"))
    pdf.setLineWidth(1.5)

    pdf.line(
        width / 2 - 170,
        height - 277,
        width / 2 + 170,
        height - 277
    )

    # =========================================
    # WORKSHOP
    # =========================================

    pdf.setFillColor(colors.HexColor("#333333"))
    pdf.setFont("Helvetica", 14)

    pdf.drawCentredString(
        width / 2,
        height - 315,
        "for successfully participating in"
    )

    pdf.setFillColor(colors.HexColor("#17365D"))
    pdf.setFont("Helvetica-Bold", 21)

    pdf.drawCentredString(
        width / 2,
        height - 350,
        workshop
    )

    # =========================================
    # DATE
    # =========================================

    pdf.setFillColor(colors.HexColor("#444444"))
    pdf.setFont("Helvetica", 12)

    pdf.drawCentredString(
        width / 2,
        height - 385,
        "Date: " + date
    )

    # =========================================
    # SIGNATURE
    # =========================================

    signature_x = 180
    signature_y = 82

    # Signature name
    pdf.setFillColor(colors.HexColor("#17365D"))
    pdf.setFont("Helvetica-Oblique", 17)

    pdf.drawCentredString(
        signature_x,
        signature_y + 25,
        signature
    )

    # Signature line
    pdf.setStrokeColor(colors.HexColor("#333333"))
    pdf.setLineWidth(1)

    pdf.line(
        105,
        signature_y + 15,
        255,
        signature_y + 15
    )

    # Label
    pdf.setFillColor(colors.HexColor("#444444"))
    pdf.setFont("Helvetica", 10)

    pdf.drawCentredString(
        signature_x,
        signature_y - 2,
        "AUTHORIZED SIGNATURE"
    )

    # =========================================
    # SEAL
    # =========================================

    seal_x = width / 2
    seal_y = 82

    # Outer circle
    pdf.setStrokeColor(colors.HexColor("#C49A3A"))
    pdf.setLineWidth(4)

    pdf.circle(
        seal_x,
        seal_y,
        34,
        fill=0,
        stroke=1
    )

    # Inner circle
    pdf.setFillColor(colors.HexColor("#17365D"))

    pdf.circle(
        seal_x,
        seal_y,
        27,
        fill=1,
        stroke=0
    )

    pdf.setFillColor(colors.white)
    pdf.setFont("Helvetica-Bold", 9)

    pdf.drawCentredString(
        seal_x,
        seal_y + 4,
        "WORKSHOP"
    )

    pdf.drawCentredString(
        seal_x,
        seal_y - 8,
        "2026"
    )

    # =========================================
    # MADE BY
    # =========================================

    pdf.setFillColor(colors.HexColor("#777777"))
    pdf.setFont("Helvetica-Oblique", 9)

    pdf.drawRightString(
        width - 75,
        62,
        "Made by Lekhani"
    )

    # =========================================
    # SAVE PDF
    # =========================================

    pdf.save()

    messagebox.showinfo(
        "Certificate Generated",
        "Certificate generated successfully!\n\n"
        + file_name
    )


# =================================================
# APPLICATION WINDOW
# =================================================

root = tk.Tk()

root.title("Professional College Certificate Generator")
root.geometry("680x680")

root.configure(bg="#E8EDF2")


# =================================================
# HEADING
# =================================================

title = tk.Label(
    root,
    text="🎓 Certificate Generator",
    font=("Arial", 24, "bold"),
    bg="#E8EDF2",
    fg="#17365D"
)

title.pack(pady=(20, 3))


subtitle = tk.Label(
    root,
    text="A4 Landscape • Professional Workshop Certificate",
    font=("Arial", 10),
    bg="#E8EDF2",
    fg="#666666"
)

subtitle.pack(pady=(0, 15))


# =================================================
# FORM
# =================================================

form = tk.Frame(
    root,
    bg="white",
    padx=35,
    pady=18
)

form.pack(
    padx=55,
    fill="x"
)


def create_field(label_text):

    label = tk.Label(
        form,
        text=label_text,
        font=("Arial", 10, "bold"),
        bg="white",
        fg="#17365D"
    )

    label.pack(anchor="w", pady=(5, 2))

    entry = tk.Entry(
        form,
        font=("Arial", 11),
        relief="solid",
        bd=1
    )

    entry.pack(
        fill="x",
        ipady=5
    )

    return entry


name_entry = create_field("Participant Name")

workshop_entry = create_field("Workshop Name")

college_entry = create_field("College / Institute Name")

date_entry = create_field("Date")

signature_entry = create_field("Signature")


# =================================================
# BUTTON
# =================================================

generate_button = tk.Button(
    root,
    text="GENERATE CERTIFICATE",
    command=generate_certificate,
    font=("Arial", 12, "bold"),
    bg="#17365D",
    fg="white",
    activebackground="#C49A3A",
    activeforeground="white",
    padx=35,
    pady=11,
    relief="flat",
    cursor="hand2"
)

generate_button.pack(pady=20)


# =================================================
# FOOTER
# =================================================

footer = tk.Label(
    root,
    text="Enter details → Generate PDF → Print / Share",
    font=("Arial", 9, "italic"),
    bg="#E8EDF2",
    fg="#777777"
)

footer.pack()


root.mainloop()