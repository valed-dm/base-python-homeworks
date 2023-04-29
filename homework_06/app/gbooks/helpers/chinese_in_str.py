import re


def if_chinese_in_str(sample):
    chinese_symbols = []
    for item in re.findall(r'[\u4e00-\u9fff]+', sample):
        chinese_symbols.append(item)

    print(chinese_symbols)
    return True if len(chinese_symbols) > 0 else False


if __name__ == '__main__':
    if_chinese_in_str('AI開發的機器學習系統設計模式(電子書)')
