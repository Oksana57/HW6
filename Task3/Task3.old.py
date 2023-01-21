str1='9*x^5+4*x^4+3*x^2+7*x+5=0'            
str2='4*x^5+7*x^4+9*x^2+2*x+6=0'  

print(str1)
print(str2)
def str_to_list(strA):
    strA = ''.join(strA)
    str10=strA.replace('*x^', '').replace('+', '').replace('=0\n', '')
    m_list = str10.split(' ')
    return m_list

print(str_to_list(str1))
print(str_to_list(str2))

def list_of_key(m_list):
    new_list = []
    for i in range(1, len(m_list)):
        if i%2!=0:
            m_list[i]=int(m_list[i])
            new_list.append(m_list[i])
        elif i+1==len(m_list):
            new_list.append(0)   
    return new_list


def list_of_means(m_list):
    new_list = []
    for i in range(0, len(m_list)+1):
        if i%2==0:
            m_list[i]=int(m_list[i])
            new_list.append(m_list[i]) 
    return new_list


def sum_poly(list1, list2, list1_1, list2_1):
    sum=0
    alist=[]
    for i in range(0, len(list1)):
        if list1[i]==list2[i]:
            sum+=list1_1[i]+list2_1[i]
            alist.append(sum)
            sum=0
    return alist

def polinomial(alist, alist1):
  
    with open('sum_poly1.txt', 'a', encoding='utf-8') as m_file3:
        poly_list=''
        for i in range(0, len(alist)):
            value = alist1[i]
            s=alist[i]
            if alist[i]>1:
                poly_list+=f"{value} *x^{s} + "
            elif alist[i]==1:
                poly_list+=f"{value} *x + "
            elif alist[i]==0:
                poly_list+=f"{value} = 0"
    
        return poly_list


m_list1 = str_to_list(str1)
m_list2 = str_to_list(str2)
l_o_k = list_of_key(m_list1)

l_o_k1 = list_of_key(m_list2)
l_o_m = list_of_means(m_list1)
l_o_m1 = list_of_means(m_list2)


s_p =sum_poly(l_o_k, l_o_k1, l_o_m, l_o_m1)


poly_list3 = polinomial(l_o_k, s_p)
print(poly_list3)

