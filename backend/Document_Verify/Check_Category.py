from openai import OpenAI
from typing import List, Tuple
import env

client = OpenAI()

def API_check_category(ocr_text: str, document_description: str) -> Tuple[bool, List[str]]:
    """
    OpenAI API로부터 문서 내용과 description이 일치하는지 검사, 문서로부터 카테고리 추출하여 DB에 저장

    Return:
        bool: 올바른 카테고리인지 검사. 1: 정상, 0: 비정상 문서, -1: 에러
        List[str]: 문서 카테고리 리스트
    """
    try:
        messages = [
            {"role": "system", "content": "You are a helpful assistant. Prompt Can Be Korean, but You should speak English Only."},
            {"role": "user", "content": f"The following is the OCR text from a document. (It is a bit noisy):\n{ocr_text}"},
            {"role": "user", "content": f"Does the general topic of this text match the following description?\n{document_description}"},
            {"role": "user", "content": "Please answer with 'yes' or 'no' and provide categories of the document if available.\n \
                                        When writing categories, you should write in the format: \"Categories: apple, banana, tree\"."}
                    ]

        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=150
        )

        output_text = response.choices[0].message.content

        print(f"\nGPT response: {output_text}\n")

        # 결과 처리
        if "yes" in output_text.lower():
            result = 1
            categories = extract_categories(output_text.lower())
        elif "no" in output_text.lower():
            result = 0
            categories = extract_categories(output_text.lower())
        else:
            result = -1
            categories = []

        return (result, categories)

    except Exception as e:
        print(f"An error occurred: {e}")
        return (-1, [])

def extract_categories(text: str) -> List[str]:
    """
    Helper function to extract categories from the GPT response text.
    This function assumes categories are listed after the confirmation.
    """
    categories = []
    if "categories" in text:
        parts = text.split("categories:")[1].strip()
        categories = [category.strip() for category in parts.split(",")]
    return categories



if __name__=="__main__":
    ocr_text = """
    Workplace Safety Protocols

    1. Always wear appropriate personal protective equipment (PPE) such as gloves, helmets, and safety glasses.
    2. Report any unsafe conditions or hazards to your supervisor immediately.
    3. Follow proper procedures for handling and disposing of hazardous materials.
    4. Participate in regular safety training sessions and drills.
    5. Keep work areas clean and free of clutter to prevent accidents.
    6. Use machinery and tools only if you are trained and authorized to do so.
    7. Adhere to all safety signs and warnings posted in the workplace.
    8. In case of an emergency, follow the established evacuation routes and procedures.
    9. Maintain proper posture and lifting techniques to avoid injuries.
    10. Ensure that emergency exits and pathways are always unobstructed.

    By following these protocols, we can ensure a safer workplace for everyone.
    """
    document_description = "This document describes the safety protocols in the workplace."
    result, categories = API_check_category(ocr_text, document_description)
    print(result, categories)