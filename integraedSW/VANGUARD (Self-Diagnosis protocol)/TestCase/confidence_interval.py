import matplotlib.pyplot as plt
import os

def get_subdir(path): # 해당 디렉토리에서 sub 디렉토리만을 찾아서 리스트로 반환하는 함수
    content_list = os.listdir(path)
    subdir_list = []
    for content in content_list:
            fullname = os.path.join(path, content)                
            if os.path.isdir(fullname):
                    subdir_list.append(fullname)
    return subdir_list

def get_file(path,file_format="all"): # 해당 디렉토리에서 특정 포맷의 파일만 찾아서 리스트로 반환하는 함수    
    file_list = os.listdir(path)
    if file_format != "all":
        format_file_list = [file for file in file_list if file.endswith(file_format)]

    else:
        format_file_list = file_list

    for i in range(len(format_file_list)):
        format_file_list[i] = os.path.join(path, format_file_list[i])           
    return format_file_list

if __name__ == "__main__":
    current = os.getcwd()
    sub_list = get_subdir(current)
    f_list = []
    for subdir in sub_list:
        f_list += get_file(subdir)

    accel_file_list = []
    brake_file_list = []
    
    for f in f_list:
        if 'accel' in f:
            accel_file_list.append(f)
        elif 'brake' in f:
            brake_file_list.append(f)   

    #accel_time = []
    APS_ACT_Feedback = dict()
    APS_Feedback = dict()
    
    #brake_time = []
    BPS_ACT_Feedback = dict()
    BPS_Feedback = dict()
    
    for i in range(len(accel_file_list)):
        f = open(f"{accel_file_list[i]}", 'r')
        lines = f.readlines()        
        for line in lines:
            temp = line.split(',')
            #accel_time.append(temp[0])
            APS_ACT_Feedback[float(temp[0])] = float(temp[1])
            APS_Feedback[float(temp[0])] = float(temp[2])
        f.close()

    for i in range(len(brake_file_list)):
        f = open(f"{brake_file_list[i]}", 'r')
        lines = f.readlines()        
        for line in lines:
            temp = line.split(',')
            #brake_time.append(temp[0])
            BPS_ACT_Feedback[float(temp[0])] = float(temp[1])
            BPS_Feedback[float(temp[0])] = float(temp[2])
        f.close()
    
    BPS_ACT_Feed_list = sorted(BPS_ACT_Feedback.items())
    
    x, y = zip(*BPS_ACT_Feed_list)

    print(x)
    print(len(x))
    print(len(y))

    plt.figure()
    plt.scatter(x,y,color='deeppink')
    plt.title("BPS_ACT_Feedback TestCase",fontsize=25)
    plt.xlabel("Test Time",fontsize=25)
    plt.ylabel("BPS_ACT_Feedback",fontsize=25)

    plt.show()


