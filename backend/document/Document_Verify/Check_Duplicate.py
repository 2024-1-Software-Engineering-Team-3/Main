import subprocess

DEDUP_ALGORITHM = 'exact_hash'
DATA_CSV_PATH = 'test_dataset.csv'

def API_check_not_duplicate(ocr_text:str) -> bool:
    """
    OCR 결과로부터 DB 상에 유사 문서가 있는지 검사, 
    """

    #DB write format (temporailly)
    write_format = f"\ndummy, {ocr_text}, dummy"

    with open(f'../data/{DATA_CSV_PATH}', mode='r', newline='', encoding='utf-8') as file:
        reader = file.readlines(2**20)

    reader.append(write_format)
    with open(f'../data/{DATA_CSV_PATH}','w', newline='', encoding='utf-8') as writer:
         writer.writelines(reader)
    
    result = check_not_duplicate()

    return result


def check_not_duplicate():
    """
    check document duplicate. if duplicated, return 0
    else return 1 (success)
    """
    command = [
        "python", "-m", f"text_dedup.{DEDUP_ALGORITHM}",
        "--path", f"../data/{DATA_CSV_PATH}",
        "--name", "gl",
        "--split", "train",
        "--cache_dir", "./cache",
        "--output", "../data/dummy",
        "--column", "text",
        "--batch_size", "10000",
        "--use_auth_token", "true",
        "--local"
    ]
    result = subprocess.run(command, capture_output=True, text=True)

    if(result.stdout.startswith('0')):
        return 0
    else:
        return 1



if __name__=="__main__":
    ocr = PororoOcr()
def get_ocr(image_path:str) ->str:
    text = ocr.run_ocr(image_path, debug=False)
    return text

def text_process(text):
    pattern = r'[.,\"\'\(\)]'
    processed_text = re.sub(pattern, '', text)
    return processed_text

if __name__=="__main__":
    
    from pororoocr import PororoOcr
    import subprocess
    import csv
    import re

    DEDUP_ALGORITHM = 'exact_hash'
    DATA_CSV_PATH = 'test_dataset.csv'
    DATA_IMAGE_PATH = 'test.jpg'
    import time
    start = time.time()
    print(f"start")

    ocr_list = get_ocr(f"../data/{DATA_IMAGE_PATH}")
    
    ocr_text = text_process(' '.join(ocr_list))

    result = API_check_not_duplicate(ocr_text)

    end = time.time()
    print(f"end, time taken: {end-start}")

    print(f"ocr result: {ocr_text}")
    print(f"duplicated result: {result} (0: not duplicated, 1: duplicated)")