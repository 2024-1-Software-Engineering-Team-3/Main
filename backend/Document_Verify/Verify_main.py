from Check_Duplicate import API_check_not_duplicate
from Check_Category import API_check_category

from typing import Tuple,List
import csv
import re
from pororoocr import PororoOcr
from concurrent.futures import ThreadPoolExecutor, as_completed

def API_Document_Verify(image_path:str,
                        document_description:str) -> Tuple[bool,bool,str, List[str]]:
    """
    image path로부터 올바른 문서인지 검사 후 결과 return

    Return:
        Tuple[bool,bool,str]
        first bool: 문서 중복 여부 (1: 정상 문서, 0: 에러)
        second bool: 문서 카테고리 정상 여부 (1: 정상 문서, 0: 에러)
        third str: message
        fourth List[str]: 문서 카테고리를 모아둔 List

    """
    ocr_list = get_ocr(image_path)
    ocr_text = text_process(' '.join(ocr_list))

    print(f"text: {ocr_text}")

    #하나는 CPU, 하나는 OpenAI api이므로 병렬로 처리하여 속도 개선
    with ThreadPoolExecutor() as executor:
        future_duplicate = executor.submit(API_check_not_duplicate, ocr_text)
        future_category = executor.submit(API_check_category, ocr_text, document_description)
        
        check_duplicate_result = future_duplicate.result()
        (check_category_result, category) = future_category.result()


    if(-1 in [check_category_result,check_duplicate_result]):
        return (0, 0, "예상치 못한 에러가 발생하였습니다. 다시 시도해주세요", None)

    elif(check_duplicate_result and check_category_result):
        return (1, 1, "Success", category)

    elif (not check_duplicate_result and check_category_result):
        return (1, 0, "과거 존재하는 자료이거나, 저작권이 존재하는 자료입니다.", None)

    elif (not check_category_result and check_duplicate_result):
        return (0, 1, "해당 문서의 카테고리가 올바르지 않습니다.", None)
    
    else:
        return (0, 0, "카테고리 검사 및 자료 유효성 검사를 통과하지 못하였습니다.", None)



ocr = PororoOcr()
def get_ocr(image_path:str) ->str:
    text = ocr.run_ocr(image_path, debug=False)
    return text

def text_process(text):
    pattern = r'[.,\"\'\(\)]'
    processed_text = re.sub(pattern, '', text)
    return processed_text


if __name__ == "__main__":
    import time
    start = time.time()
    print("---------------start test-----------------------------------------------\n")
    
    document_description = "This document outlines the implementation of the Golden Time system for disaster response"
    print(API_Document_Verify('../data/test.jpg',document_description))
    
    end = time.time()
    print(f"\n------------------------ end, time taken of API: {end-start} ----------")