from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from link import *
from api.sql import *
import imp, random, os, string
from werkzeug.utils import secure_filename
from flask import current_app
import datetime

UPLOAD_FOLDER = 'static/product'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

manager = Blueprint('manager', __name__, template_folder='../templates')

def config():
    current_app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    config = current_app.config['UPLOAD_FOLDER'] 
    return config

@manager.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return redirect(url_for('manager.productManager'))

@manager.route('/productManager', methods=['GET', 'POST'])
@login_required
def productManager():
    if request.method == 'GET':
        if(current_user.role == 'user'):
            flash('No permission')
            return redirect(url_for('index'))
        
    if 'delete' in request.values:
        pno = request.values.get('delete')
        data = Product.delete_product(pno)
        
        if(data != None):
            flash('failed')
        else:
            data = Product.get_patient(pno)
            Product.delete_product(pno)
    
    elif 'edit' in request.values:
        pno = request.values.get('edit')
        return redirect(url_for('manager.edit', pno=pno))
    
    patient_data = patient()
    return render_template('productManager.html', patient_data = patient_data, user=current_user.name)

def patient():
    patient_row = Product.get_all_patient()
    patient_data = []
    for i in patient_row:
        patient = {
            '病歷編號': i[1],
            '患者姓名': i[2],
            '性別': i[3],
            '生日': i[4],
            '主治醫師':i[6],
            '狀態': i[7]
        }
        patient_data.append(patient)
    return patient_data

@manager.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = ""
        while(data != None):
            number = str(random.randrange( 10, 99))
            en = random.choice(string.ascii_letters)
            pno = 'P0' + number
            data = Product.get_patient(pno)

        name = request.values.get('name')
        birthdate = request.values.get('birthdate')
        gender = request.values.get('gender')
        description = request.values.get('description')
        doctor = request.values.get('doctor')
        discharge = request.values.get('discharge')

        if (len(name) < 1 or len(birthdate) < 1):
            return redirect(url_for('manager.productManager'))

        Product.add_patient(
            {'pno' : pno,
             'name' : name,
             'gender' : gender,
             'birthdate' : birthdate,
             'description':description,
             'doctor':doctor,
             'discharge':discharge
            }
        )

        return redirect(url_for('manager.productManager'))

    return render_template('productManager.html')

@manager.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    if request.method == 'GET':
        if(current_user.role == 'user'):
            flash('No permission')
            return redirect(url_for('bookstore'))

    if request.method == 'POST':
        Product.update_patient(
            {
            'name' : request.values.get('name'),
            'gender' : request.values.get('gender'),
            'birthdate' : request.values.get('birthdate'),
            'description' : request.values.get('description'),
            'doctor' : request.values.get('doctor'),
            'discharge' : request.values.get('discharge'),
            'pno' : request.values.get('pno')
            }
        )
        
        return redirect(url_for('manager.productManager'))

    else:
        product = show_info()
        return render_template('edit.html', data=product)


def show_info():
    pno = request.args['pno']
    data = Product.get_patient(pno)
    pname = data[2]
    birthdate = data[4]
    gender = data[3]
    description = data[5]
    doctor = data[6]
    discharge = data[7]

    product = {
        '病歷編號': pno,
        '患者姓名': pname,
        '性別': gender,
        '生日': birthdate,
        '症狀': description,
        '主治醫師':doctor,
        '狀態': discharge
    }
    return product

# _______________________________________________________________________

@manager.route('/vitalsignManager', methods=['GET', 'POST'])
@login_required
def vitalsignManager():
    if request.method == 'GET':
        if(current_user.role == 'user'):
            flash('No permission')
            return redirect(url_for('index'))
        
    if 'deletevitalsign' in request.values:
        pno = request.values.get('deletevitalsign')
        data = Product.delete_vital_sign(pno)
        
        if(data != None):
            flash('failed')
        else:
            data = Product.get_vital_sign(pno)
            Product.delete_vital_sign(pno)
    
    elif 'editvitalsign' in request.values:
        pno = request.values.get('editvitalsign')
        return redirect(url_for('manager.editvitalsign', pno=pno))
    
    vital_sign_data = vital_sign()
    return render_template('vitalsignManager.html', vital_sign_data = vital_sign_data, user=current_user.name)

def vital_sign():
    book_row = Product.get_all_vital_sign()
    book_data = []
    for i in book_row:
        book = {
            '病歷編號': i[1],
            '測量時間': i[2],
            '呼吸': i[3],
            '收縮': i[4],
            '血氧': i[5],
            '體溫': i[6],
            '預警分數': i[7],
            '風險': i[8],
            '脈搏': i[9],
        }
        book_data.append(book)
    return book_data

@manager.route('/addvitalsign', methods=['GET', 'POST'])
def addvitalsign():
    if request.method == 'POST':
        data = ""
        while(data != None):
            number = str(random.randrange( 0, 10))
            pno = 'P' + number
            data = Product.get_vital_sign(pno)

        pno = request.values.get('pno')
        rr = request.values.get('rr')
        bp = request.values.get('bp')
        spo2 = request.values.get('spo2')
        bt = request.values.get('bt')
        risk = request.values.get('risk')
        pulse = request.values.get('pulse')

        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

        Product.add_vital_sign(
            {
            'pno' : str(pno),
            'seqtime' : str(current_time),
            'rr' : str(rr),
            'bp' : str(bp),
            'spo2' : str(spo2),
            'bt' : str(bt),
            'score' : number,
            'risk' : str(risk),
            'pulse' :str(pulse)
            }
        )

        return redirect(url_for('manager.vitalsignManager'))

    return render_template('vitalsignManager.html')

@manager.route('/editvitalsign', methods=['GET', 'POST'])
@login_required
def editvitalsign():
    if request.method == 'GET':
        if(current_user.role == 'user'):
            flash('No permission')
            return redirect(url_for('bookstore'))

    if request.method == 'POST':
        Product.update_vital_sign(
            {
            'seqtime' : request.values.get('seqtime'),
            'pno' : request.values.get('pno'),
            'rr' : request.values.get('rr'),
            'bp' : request.values.get('bp'),
            'spo2' : request.values.get('spo2'),
            'bt' : request.values.get('bt'),
            'score' : request.values.get('score'),
            'risk' : request.values.get('risk'),
            'pulse' : request.values.get('pulse')
            }
        )
        
        return redirect(url_for('manager.vitalsignManager'))

    else:
        product = show_vitalsignInfo()
        return render_template('editvitalsign.html', data=product)


def show_vitalsignInfo():
    pno = request.args['pno']
    data = Product.get_vital_sign(pno)
    pno = data[1]
    seqtime = data[2]
    rr = data[3]
    bp = data[4]
    spo2 = data[5]
    bt = data[6]
    score = data[7]
    risk = data[8]
    pulse = data[9]
    print(risk)
    product = {
        '病歷編號': pno,
        '測量時間': seqtime,
        '呼吸': rr,
        '收縮': bp,
        '血氧': spo2,
        '體溫': bt,
        '預警分數': score,
        '風險': risk,
        '脈搏': pulse
    }
    return product
# _________________________________________________________________

@manager.route('/doctorManager', methods=['GET', 'POST'])
@login_required
def doctorManager():
    if request.method == 'GET':
        if(current_user.role == 'user'):
            flash('No permission')
            return redirect(url_for('index'))
        
    if 'deletedoctor' in request.values:
        dno = request.values.get('deletedoctor')
        data = Product.delete_doctor(dno)
        
        if(data != None):
            flash('failed')
        else:
            data = Product.get_doctor(dno)
            Product.delete_doctor(dno)
    
    elif 'editdoctor' in request.values:
        dno = request.values.get('editdoctor')
        return redirect(url_for('manager.editdoctor', dno=dno))
    
    doctor_data = doctor()
    return render_template('doctorManager.html', doctor_data = doctor_data, user=current_user.name)

def doctor():
    doctor_row = Product.get_all_doctor()
    doctor_data = []
    for i in doctor_row:
        doctor = {
            '醫師編號': i[1],
            '醫師姓名': i[2],
            '主治科別': i[3]
        }
        doctor_data.append(doctor)
    return doctor_data

@manager.route('/adddoctor', methods=['GET', 'POST'])
def adddoctor():
    if request.method == 'POST':
        data = ""
        while(data != None):
            number = str(random.randrange( 0, 100))
            dno = '90' + number
            data = Product.get_doctor(dno)

        dno = request.values.get('dno')
        dname = request.values.get('dname')
        dept = request.values.get('dept')
        Product.add_doctor(
            {
            'dno' : str(dno),
            'dname' : str(dname),
            'dept' :str(dept)
            }
        )

        return redirect(url_for('manager.doctorManager'))

    return render_template('doctorManager.html')

@manager.route('/editdoctor', methods=['GET', 'POST'])
@login_required
def editdoctor():
    if request.method == 'GET':
        if(current_user.role == 'user'):
            flash('No permission')
            return redirect(url_for('bookstore'))

    if request.method == 'POST':
        Product.update_doctor(
            {
            'dno' : request.values.get('dno'),
            'dname' : request.values.get('dname'),
            'dept' : request.values.get('dept')
            }
        )
        
        return redirect(url_for('manager.doctorManager'))

    else:
        doctorInfo = show_doctorInfo()
        return render_template('editdoctor.html', data=doctorInfo)


def show_doctorInfo():
    dno = request.args['dno']
    data = Product.get_doctor(dno)
    dno = data[1]
    dname = data[2]
    dept = data[3]

    doctor = {
        '醫師編號': dno,
        '醫師姓名': dname,
        '主治科別': dept
    }
    return doctor
# ________________________________________________________________________
@manager.route('/bedManager', methods=['GET', 'POST'])
@login_required
def bedManager():
    if request.method == 'GET':
        if(current_user.role == 'user'):
            flash('No permission')
            return redirect(url_for('index'))
        
    if 'deletebed' in request.values:
        bno = request.values.get('deletebed')
        data = Product.delete_bed(bno)
        
        if(data != None):
            flash('failed')
        else:
            data = Product.get_bed(bno)
            Product.delete_bed(bno)
    
    elif 'editbed' in request.values:
        bno = request.values.get('editbed')
        return redirect(url_for('manager.editbed', bno=bno))
    
    bed_data = bed()
    return render_template('bedManager.html', bed_data = bed_data, user=current_user.name)

def bed():
    bed_row = Product.get_all_bed()
    bed_data = []
    for i in bed_row:
        bed = {
            '病床號': i[1],
            '病歷編號': i[2],
            '住院開始時間': i[3],
            '住院結束時間': i[4],
        }
        bed_data.append(bed)
    return bed_data

@manager.route('/add_bed', methods=['GET', 'POST'])
def add_bed():
    if request.method == 'POST':
        data = ""
        while(data != None):
            number = str(random.randrange( 0, 10))
            bno = 'B' + number
            data = Product.get_bed(bno)

        bno = request.values.get('bno')
        pno = request.values.get('pno')
        starttime = request.values.get('starttime')
        endtime = request.values.get('endtime')
        Product.add_bed(
            {
            'bno' : str(bno),
            'pno' : str(pno),
            'starttime' :str(starttime),
            'endtime' :str(endtime)
            }
        )

        return redirect(url_for('manager.bedManager'))

    return render_template('bedManager.html')

@manager.route('/editbed', methods=['GET', 'POST'])
@login_required
def editbed():
    if request.method == 'GET':
        if(current_user.role == 'user'):
            flash('No permission')
            return redirect(url_for('bookstore'))

    if request.method == 'POST':
        Product.update_bed(
            {
            'bno' : request.values.get('bno'),
            'pno' : request.values.get('pno'),
            'starttime' : request.values.get('starttime'),
            'endtime' : request.values.get('endtime')
            }
        )
        
        return redirect(url_for('manager.bedManager'))

    else:
        bed = show_bedInfo()
        return render_template('editbed.html', data=bed)


def show_bedInfo():
    bno = request.args['bno']
    data = Product.get_bed(bno)

    bno = data[1]
    pno = data[2]
    starttime = data[3]
    endtime = data[4]

    bed = {
        '病床號': bno,
        '病歷編號': pno,
        '住院開始時間': starttime,
        '住院結束時間': endtime
    }
    return bed


@manager.route('/orderManager', methods=['GET', 'POST'])
@login_required
def orderManager():
    if request.method == 'POST':
        pass
    else:
        order_row = Order_List.get_order()
        order_data = []
        for i in order_row:
            order = {
                '訂單編號': i[0],
                '訂購人': i[1],
                '訂單總價': i[2],
                '訂單時間': i[3]
            }
            order_data.append(order)
            
        orderdetail_row = Order_List.get_orderdetail()
        order_detail = []

        for j in orderdetail_row:
            orderdetail = {
                '訂單編號': j[0],
                '商品名稱': j[1],
                '商品單價': j[2],
                '訂購數量': j[3]
            }
            order_detail.append(orderdetail)

    return render_template('orderManager.html', orderData = order_data, orderDetail = order_detail, user=current_user.name)