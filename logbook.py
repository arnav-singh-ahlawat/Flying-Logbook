from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import mysql.connector

class Logbook:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('Flying Logbook')

        #Variables
        self.var_sn=StringVar()
        self.var_id=StringVar()
        self.var_rank=StringVar()
        self.var_name=StringVar()
        self.var_squadron=StringVar()
        self.var_aircraft=StringVar()
        self.var_tail=StringVar()
        self.var_depart=StringVar()
        self.var_arrive=StringVar()
        self.var_date=StringVar()
        self.var_from=IntVar()
        self.var_to=IntVar()
        self.var_duration=DoubleVar()
        self.var_remarks=StringVar()

        #Title
        lbl_title=Label(self.root, text="FLYING LOGBOOK ✈📘", font=('tahoma', 28, 'bold', 'italic'), fg='#222222', bg='lightblue')
        lbl_title.place(x=0, y=0, width=1530, height=60)

        #IAF Logo
        img_logo=Image.open('Images/iaf_logo.jpg')
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root, image=self.photo_logo)
        self.logo.place(x=25, y=5, width=50, height=50)

        # Image Frame
        img_frame = Image.open('Images/frame.jpg')
        self.photo_frame = ImageTk.PhotoImage(img_frame)

        img_frame = Label(self.root, image=self.photo_frame)
        img_frame.place(x=0, y=60, width=1530, height=150)

        #Main Frame
        main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        main_frame.place(x=10, y=210, width=1500, height=560)

        #Upper Frame
        upper_frame = LabelFrame(main_frame, relief=RIDGE, bg='white', text='Sortie (Flight) Details:', font=('arial', 11, 'bold'), fg='red')
        upper_frame.place(x=10, y=10, width=1480, height=270)

        #Input Fields

        #ID No
        lbl_id = Label(upper_frame, text='ID No - ', font=('arial', 11, 'bold'), bg='white', fg='black')
        lbl_id.grid(row=0, column=0, padx=2, pady=7, sticky=W)

        txt_id = Entry(upper_frame, textvariable=self.var_id, width=22, font=('arial', 10))
        txt_id.grid(row=0, column=1, padx=2, pady=7)

        #Rank
        lbl_rank = Label(upper_frame, text='Rank - ', font=('arial', 11, 'bold'), bg='white', fg='black')
        lbl_rank.grid(row=1, column=0, padx=2, pady=7, sticky=W)

        combo_rank = Combobox(upper_frame, textvariable=self.var_rank, font=('arial', 11), width=17, state='readonly')
        combo_rank['value'] = ('Select Rank', 'Fg Offr', 'Flt Lt', 'Sqn Ldr', 'Wg Cdr', 'Gp Capt')
        combo_rank.current(0)
        combo_rank.grid(row=1, column=1, padx=2, pady=7, sticky=W)

        #Name
        lbl_name = Label(upper_frame, text='Name - ', font=('arial', 11, 'bold'), bg='white', fg='black')
        lbl_name.grid(row=2, column=0, padx=2, pady=7, sticky=W)

        txt_name = Entry(upper_frame, textvariable=self.var_name, width=22, font=('arial', 10))
        txt_name.grid(row=2, column=1, padx=2, pady=7)

        #Squadron
        lbl_squadron = Label(upper_frame, text='Squadron - ', font=('arial', 11, 'bold'), bg='white', fg='black')
        lbl_squadron.grid(row=3, column=0, padx=2, pady=7, sticky=W)

        txt_squadron = Entry(upper_frame, textvariable=self.var_squadron, width=22, font=('arial', 10))
        txt_squadron.grid(row=3, column=1, padx=2, pady=7)

        #Aircraft
        lbl_aircraft = Label(upper_frame, text='Aircraft - ', font=('arial', 11, 'bold'), bg='white', fg='black')
        lbl_aircraft.grid(row=0, column=2, padx=2, pady=7, sticky=W)

        txt_aircraft = Entry(upper_frame, textvariable=self.var_aircraft, width=22, font=('arial', 10))
        txt_aircraft.grid(row=0, column=3, padx=2, pady=7)

        #Tail No
        lbl_tail = Label(upper_frame, text='Tail No - ', font=('arial', 11, 'bold'), bg='white', fg='black')
        lbl_tail.grid(row=1, column=2, padx=2, pady=7, sticky=W)

        txt_tail = Entry(upper_frame, textvariable=self.var_tail, width=22, font=('arial', 10))
        txt_tail.grid(row=1, column=3, padx=2, pady=7)

        #Departing Station
        lbl_depart = Label(upper_frame, text='Departing Station - ', font=('arial', 11, 'bold'), bg='white', fg='black')
        lbl_depart.grid(row=2, column=2, padx=2, pady=7, sticky=W)

        txt_depart = Entry(upper_frame, textvariable=self.var_depart, width=22, font=('arial', 10))
        txt_depart.grid(row=2, column=3, padx=2, pady=7)

        #Arriving Station
        lbl_arrive = Label(upper_frame, text='Arriving Station - ', font=('arial', 11, 'bold'), bg='white', fg='black')
        lbl_arrive.grid(row=3, column=2, padx=2, pady=7, sticky=W)

        txt_arrive = Entry(upper_frame, textvariable=self.var_arrive, width=22, font=('arial', 10))
        txt_arrive.grid(row=3, column=3, padx=2, pady=7)

        #Date
        lbl_date = Label(upper_frame, text='Date - ', font=('arial', 11, 'bold'), bg='white', fg='black')
        lbl_date.grid(row=0, column=4, padx=2, pady=7, sticky=W)

        txt_date = Entry(upper_frame, textvariable=self.var_date, width=22, font=('arial', 10))
        txt_date.grid(row=0, column=5, padx=2, pady=7)

        #From
        lbl_from = Label(upper_frame, text='From (2400 hrs) - ', font=('arial', 11, 'bold'), bg='white', fg='black')
        lbl_from.grid(row=1, column=4, padx=2, pady=7, sticky=W)

        txt_from = Entry(upper_frame, textvariable=self.var_from, width=22, font=('arial', 10))
        txt_from.grid(row=1, column=5, padx=2, pady=7)

        #To
        lbl_to = Label(upper_frame, text='To (2400 hrs) - ', font=('arial', 11, 'bold'), bg='white', fg='black')
        lbl_to.grid(row=2, column=4, padx=2, pady=7, sticky=W)

        txt_to = Entry(upper_frame, textvariable=self.var_to, width=22, font=('arial', 10))
        txt_to.grid(row=2, column=5, padx=2, pady=7)

        #Remarks
        lbl_remarks = Label(upper_frame, text='Remarks - ', font=('arial', 11, 'bold'), bg='white', fg='black')
        lbl_remarks.grid(row=4, column=0, padx=2, pady=7, sticky=W)

        txt_remarks = Entry(upper_frame, textvariable=self.var_remarks, width=66, font=('arial', 10))
        txt_remarks.grid(row=4, column=1, columnspan=3, padx=2, pady=7)

        #Buttons
        button_frame=Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=1330, y=10, width=125, height=172)

        btn_add=Button(button_frame, text="Save", command=self.add_entry, font=("arial", 11, "bold"), width=12, bg='#5d8aa8', fg='white')
        btn_add.grid(row=0, column=0, padx=1, pady=5)

        btn_update = Button(button_frame, text="Update", command=self.update_entry, font=("arial", 11, "bold"), width=12, bg='#5d8aa8', fg='white')
        btn_update.grid(row=1, column=0, padx=1, pady=5)

        btn_delete = Button(button_frame, text="Delete", command=self.delete_entry, font=("arial", 11, "bold"), width=12, bg='#5d8aa8', fg='white')
        btn_delete.grid(row=2, column=0, padx=1, pady=5)

        btn_reset = Button(button_frame, text="Reset", command=self.reset_entries, font=("arial", 11, "bold"), width=12, bg='#5d8aa8', fg='white')
        btn_reset.grid(row=3, column=0, padx=1, pady=5)

        #Lower  Frame
        lower_frame = LabelFrame(main_frame, relief=RIDGE, bg='white', text='Sortie (Flight) Entries:', font=('arial', 11, 'bold'), fg='red')
        lower_frame.place(x=10, y=280, width=1480, height=270)

        #Search Frame
        search_frame = LabelFrame(lower_frame, bd=2, relief=RIDGE, bg='#666666')
        search_frame.place(x=3, y=0, width=1470, height=40)

        search_by=Label(search_frame, font=('arial', 11, 'bold'), text='Search by:', fg='white', bg='#666666')
        search_by.grid(row=0, column=0, sticky=W, padx=5, pady=6)

        #Search Options
        self.var_com_search = StringVar()
        com_txt_search = ttk.Combobox(search_frame, textvariable=self.var_com_search, state='readonly', font=('arial', 11), width=18)
        com_txt_search['value'] = ('Select Option', 'ID No', 'Aircraft', 'Squadron', 'Departing Station', 'Arriving Station')
        com_txt_search.current(0)
        com_txt_search.grid(row=0, column=1, sticky=W, padx=5)

        self.var_search = StringVar()
        txt_search = ttk.Entry(search_frame, textvariable=self.var_search, width=22, font=('arial', 11))
        txt_search.grid(row=0, column=2, padx=5)

        btn_search = Button(search_frame, text='Search', command=self.search_entries, font=("arial", 11, "bold"), width=14, bg='#5d8aa8', fg='white')
        btn_search.grid(row=0, column=3, padx=5)

        btn_showall = Button(search_frame, text='Show All', command=self.display_logbook, font=("arial", 11, "bold"), width=14, bg='#5d8aa8', fg='white')
        btn_showall.grid(row=0, column=4, padx=5)

        #Table Frame
        table_frame = Frame(lower_frame, bd=3, relief=RIDGE)
        table_frame.place(x=0, y=40, width=1470, height=210)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.logbook_table = ttk.Treeview(table_frame, columns=(
        'sn', 'id', 'rank', 'name', 'squadron', 'aircraft', 'tail', 'depart', 'arrive', 'date', 'from', 'to', 'duration', 'remarks'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.config(command=self.logbook_table.xview)
        scroll_y.config(command=self.logbook_table.yview)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.logbook_table.heading('sn', text='Sortie No')
        self.logbook_table.heading('id', text='ID No')
        self.logbook_table.heading('rank', text='Rank')
        self.logbook_table.heading('name', text='Name')
        self.logbook_table.heading('squadron', text='Squadron')
        self.logbook_table.heading('aircraft', text='Aircraft')
        self.logbook_table.heading('tail', text='Tail No')
        self.logbook_table.heading('depart', text='Departing Station')
        self.logbook_table.heading('arrive', text='Arriving Station')
        self.logbook_table.heading('date', text='Date')
        self.logbook_table.heading('from', text='From')
        self.logbook_table.heading('to', text='To')
        self.logbook_table.heading('duration', text='Duration (hrs)')
        self.logbook_table.heading('remarks', text='Remarks')

        self.logbook_table.pack(fill=BOTH, expand=1)

        self.logbook_table['show'] = 'headings'

        self.logbook_table.column('sn', width=40)
        self.logbook_table.column('id', width=40)
        self.logbook_table.column('rank', width=20)
        self.logbook_table.column('name', width=100)
        self.logbook_table.column('squadron', width=10)
        self.logbook_table.column('aircraft', width=100)
        self.logbook_table.column('tail', width=15)
        self.logbook_table.column('depart', width=45)
        self.logbook_table.column('arrive', width=40)
        self.logbook_table.column('date', width=35)
        self.logbook_table.column('from', width=5)
        self.logbook_table.column('to', width=5)
        self.logbook_table.column('duration', width=25)
        self.logbook_table.column('remarks', width=200)

        self.logbook_table.pack(fill=BOTH, expand=1)
        self.logbook_table.bind("<ButtonRelease>", self.get_cursor)

        self.display_logbook()

    #Methods

    #Add Entry
    def add_entry(self):
        if self.var_id.get()=="" or self.var_date.get()=="":
            messagebox.showerror('Error', 'All Fields are required')
        else:
            try:
                # To Calculate Duration
                from_time = int(self.var_from.get())
                to_time = int(self.var_to.get())

                # Convert 2400 format to regular time format
                from_time_hours = from_time // 100
                from_time_minutes = from_time % 100
                to_time_hours = to_time // 100
                to_time_minutes = to_time % 100

                # Calculate duration
                if from_time <= to_time:
                    hours = to_time_hours - from_time_hours
                    minutes = to_time_minutes - from_time_minutes
                    if minutes < 0:
                        hours -= 1
                        minutes += 60
                else:
                    hours = 24 - from_time_hours + to_time_hours
                    minutes = to_time_minutes - from_time_minutes
                    if minutes < 0:
                        hours -= 1
                        minutes += 60

                duration = hours + minutes / 60.0

                #To Generate Sortie No based on ID No and Date
                service_no = self.var_id.get()
                date = self.var_date.get()
                sortie_number = "(" + service_no + ")" + date

                self.var_sn.set(sortie_number)
                self.var_duration.set(duration)

                connection=mysql.connector.connect(host='localhost',user='root',password='password',database='fg_log')
                cursor=connection.cursor()
                cursor.execute('insert into logbook values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (self.var_sn.get(), self.var_id.get(), self.var_rank.get(), self.var_name.get(), self.var_squadron.get(), self.var_aircraft.get(), self.var_tail.get(), self.var_depart.get(), self.var_arrive.get(), self.var_date.get(), self.var_from.get(), self.var_to.get(), self.var_duration.get(), self.var_remarks.get()))

                connection.commit()
                self.display_logbook()
                connection.close()
                messagebox.showinfo('Success', 'Entry Inserted')

            except Exception as e:
                messagebox.showerror('Error', f'Something went wrong: {str(e)}', parent=self.root)

    #Display Logbook
    def display_logbook(self):
        connection = mysql.connector.connect(host='localhost', user='root', password='password', database='fg_log')
        cursor = connection.cursor()
        cursor.execute('select * from logbook')
        data = cursor.fetchall()
        if len(data) > 0:
            self.logbook_table.delete(*self.logbook_table.get_children())
            for i in data:
                self.logbook_table.insert('', 'end', values=i)
            connection.commit()
        connection.close()

    #Assigning Indices
    def get_cursor(self, event=""):
        cursor_row = self.logbook_table.focus()
        content = self.logbook_table.item(cursor_row)
        data = content['values']

        self.var_sn.set(data[0])
        self.var_id.set(data[1])
        self.var_rank.set(data[2])
        self.var_name.set(data[3])
        self.var_squadron.set(data[4])
        self.var_aircraft.set(data[5])
        self.var_tail.set(data[6])
        self.var_depart.set(data[7])
        self.var_arrive.set(data[8])
        self.var_date.set(data[9])
        self.var_from.set(data[10])
        self.var_to.set(data[11])
        self.var_duration.set(data[12])
        self.var_remarks.set(data[13])

    #Update Entry
    def update_entry(self):
        if self.var_sn.get() == "":
            messagebox.showerror('Error', 'Please select an entry to update.')
        else:
            try:
                # Delete the existing entry
                self.delete_entry()

                # Insert a new entry with updated information
                self.add_entry()

                messagebox.showinfo('Success', 'Entry updated successfully.')
            except Exception as e:
                messagebox.showerror('Error', f'Error updating entry: {str(e)}', parent=self.root)

    #Delete Entry
    def delete_entry(self):
        if self.var_sn.get() == "":
            messagebox.showerror('Error', 'Please select an entry to delete.')
        else:
            try:
                delete = messagebox.askyesno('Delete', 'Are you sure you want to delete this entry?', parent=self.root)
                if delete:
                    connection = mysql.connector.connect(host='localhost', user='root', password='password', database='fg_log')
                    cursor = connection.cursor()
                    sql = "DELETE FROM logbook WHERE sn=%s"
                    value = (self.var_sn.get(),)
                    cursor.execute(sql, value)
                else:
                    if not delete:
                        return
                connection.commit()
                self.display_logbook()
                connection.close()
                messagebox.showinfo('Deleted', 'Logbook entry successfully deleted.', parent=self.root)
            except Exception as e:
                messagebox.showerror('Error', f'Error deleting entry: {str(e)}', parent=self.root)

    #Clear Fields
    def reset_entries(self):
        self.var_sn.set("")
        self.var_id.set("")
        self.var_rank.set("Select Rank")
        self.var_name.set("")
        self.var_squadron.set("")
        self.var_aircraft.set("")
        self.var_tail.set("")
        self.var_depart.set("")
        self.var_arrive.set("")
        self.var_date.set("")
        self.var_from.set(0)
        self.var_to.set(0)
        self.var_duration.set(0.0)
        self.var_remarks.set("")

    #Search Entries
    def search_entries(self):
        search_option = self.var_com_search.get()
        search_value = self.var_search.get()

        if search_option == "Select Option" or search_value == "":
            messagebox.showerror("Error", "Please select search criteria and enter search value.")
        else:
            try:
                connection = mysql.connector.connect(host='localhost', user='root', password='password',
                                                     database='fg_log')
                cursor = connection.cursor()

                # Construct SQL query based on search criteria
                if search_option == "ID No":
                    sql = "SELECT * FROM logbook WHERE id LIKE %s"
                elif search_option == "Aircraft":
                    sql = "SELECT * FROM logbook WHERE aircraft LIKE %s"
                elif search_option == "Squadron":
                    sql = "SELECT * FROM logbook WHERE squadron LIKE %s"
                elif search_option == "Departing Station":
                    sql = "SELECT * FROM logbook WHERE depart LIKE %s"
                elif search_option == "Arriving Station":
                    sql = "SELECT * FROM logbook WHERE arrive LIKE %s"


                cursor.execute(sql, ('%' + search_value + '%',))
                data = cursor.fetchall()

                if data:
                    self.logbook_table.delete(*self.logbook_table.get_children())
                    for record in data:
                        self.logbook_table.insert('', 'end', values=record)
                else:
                    messagebox.showinfo("Not Found", "No matching entries found.")

                connection.commit()
                connection.close()

            except Exception as e:
                messagebox.showerror('Error', f'Error searching entries: {str(e)}', parent=self.root)



if __name__=="__main__":
    root=Tk()
    obj=Logbook(root)
    root.mainloop()