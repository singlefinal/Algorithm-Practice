def get_all_result(form1, form2):
    # 返回两个算式的所有可能的组合算式
    # 确保算式的数字为前大后小

    form1 = str(form1)
    form2 = str(form2)
    if eval(form1) < eval(form2):
        form1, form2 = form2, form1

    all_result = []

    for symbol in list("+-*/"):
        formula = f"({form1}{symbol}{form2})"
        try:
            eval(formula)
        except ZeroDivisionError:
            pass
        else:
            all_result.append(formula)

    return all_result


def calc_24(numlist_4):
    # 输入4个数字的列表，输出所有结果等于24的算式列表

    form_24 = []
    for i in range(4):
        for j in range(i + 1, 4):
            form1 = numlist_4[i]
            form2 = numlist_4[j]
            all_result_1 = get_all_result(form1, form2)
            numlist_3 = numlist_4[:i] + numlist_4[i + 1: j] + numlist_4[j + 1:]
            for form3 in all_result_1:
                numlist_3.append(form3)
                for x in range(3):
                    for y in range(x + 1, 3):
                        form4 = numlist_3[x]
                        form5 = numlist_3[y]
                        all_result_2 = get_all_result(form4, form5)
                        numlist_2 = numlist_3[:x] + numlist_3[x + 1: y] + numlist_3[y + 1:]
                        for form6 in all_result_2:
                            all_result_3 = get_all_result(form6, numlist_2[0])
                            for final_form in all_result_3:
                                try:
                                    result = eval(final_form)
                                except ZeroDivisionError:
                                    pass
                                else:
                                    # print(final_form + "=" + str(result))
                                    if result == 24:
                                        form_24.append(final_form)
                numlist_3.pop()
    return form_24


while True:
    nums = input("请输入4个数字，用空格分隔，退出请输入"q":")
    if nums == "q":
        break
    else:
        nums = [int(i) for i in nums.split()]
        print("所有算式组合如下:")
        for form in calc_24(nums):
            print(form + "=24")
    
