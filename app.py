from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])  # định nghĩa route cho trang chủ
def home():#sẽ gọi hàm home 
    ten = email = message = None  # khởi tạo biến ten, email, message với giá trị None
    if request.method == 'POST':  # kiểm tra nếu là phương thức POST
        ten = request.form.get('ten')  # lấy giá trị của trường 'ten' từ form
        email = request.form.get('email')  # lấy giá trị của trường 'email' từ form
        message = request.form.get('message')  # lấy giá trị của trường 'message' từ form

    return render_template ('index.html', ten=ten, email=email, message=message)#trả về nội dung của file index.html trong thư mục templates
if __name__ == '__main__':
    import os # kiểm tra nếu biến môi trường FLASK_ENV là 'development'
    port = int(os.environ.get('PORT', 5000))  # lấy cổng từ biến môi trường hoặc mặc định là 5000
    app.run(debug=False, host='0.0.0.0', port=port) # chạy ứng dụng Flask với chế độ không gỡ lỗi, lắng nghe trên tất cả các địa chỉ IP và cổng đã chỉ định