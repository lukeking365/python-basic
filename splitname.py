firstNameList=["李","王","张","刘","陈","杨","赵","黄","周","吴","徐","孙","胡","朱","高","林","何","郭","司马","司"]
def getFiristName(name):
    lenName = len(name)
    while lenName > 0:
        if name[0:lenName] in firstNameList:
            lenFirstName = len(name[0:lenName])
            print("姓："+ name[0:lenFirstName] +" 名："+ name[lenFirstName:(lenName+2)])
            break
        lenName -=1
#test
if __name__ == "__main__":
    getFiristName("高晓婷")
    getFiristName("司马慧明")
    getFiristName('司玉婷')
    getFiristName('周芳')
