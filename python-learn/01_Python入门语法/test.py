find_person = input("请你输入你要查找的用户:")
user_app = {
    '王二': {
        '购物': '淘宝',
        '娱乐': '抖音',
        '支付': '微信',
    },

    '赵四': {
        '购物': '京东',
        '娱乐': '王者荣耀',
        '支付': '支付宝',
    },
}

if find_person in user_app:
    print(f"{find_person},在该列表")
    print(user_app[find_person])
else:
    print(f"{find_person},不在该列表")
