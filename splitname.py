firstNameList=["李","王","张","刘","陈","杨","赵","黄","周","吴","徐","孙","胡","朱","高","林","何","郭","司马","司"]


def getFiristName(name):
    lenName = n = len(name)
    # n = lenName
    while n > 0:
        if name[0:n] in firstNameList:
            print("姓："+ name[0:n] +" 名："+ name[n:(lenName+1)])
            break         
        n -= 1
        if n == 0:
            print('对不起，没有找到匹配信息！')
        
def getFiristNames(names):
    for i in names:
        lenName = n = len(i)
        # n = lenName
        while n > 0:
            if i[0:n] in firstNameList:
                print("姓："+ i[0:n] +" 名："+ i[n:(lenName+1)])
                break         
            n -= 1
            if n == 0:
                print('对不起，没有找到匹配信息！')
        
if __name__ == "__main__":
    getFiristName("高晓婷")
    getFiristName("司马慧明")
    getFiristName('司玉婷')
    getFiristName('周芳')
    getFiristName('邹爱莲')
    getFiristNames(["高晓婷","司马慧明",'司玉婷','周芳','邹爱莲'])
