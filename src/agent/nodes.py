from groq import Groq
from dotenv import load_dotenv
import os
import time

from src.agent.prompts import (
    ALLOWED_TONES,
    ALLOWED_PURPOSES,
    ALLOWED_USE_CASES,
    build_grammar_prompt,
    build_refinement_prompt
)

from src.logger import logger


load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL_NAME = "llama-3.3-70b-versatile"


def call_llm(prompt: str, retries: int = 2) -> str:
    last_error = None

    for attempt in range(retries + 1):
        try:
            logger.info(f"Calling LLM. Attempt {attempt + 1}")

            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.2
            )

            output = response.choices[0].message.content.strip()

            if not output:
                raise ValueError("LLM returned an empty response.")

            logger.info("LLM response received successfully")
            return output

        except Exception as e:
            last_error = e
            logger.error(f"LLM call failed on attempt {attempt + 1}: {str(e)}")

            if attempt < retries:
                logger.info("Retrying LLM call...")
                time.sleep(1)

    logger.error("LLM call failed after all retry attempts")
    raise last_error

def validate_input(state):
    logger.info("Starting input validation")

    input_text = state.get("input_text", "").strip()
    tone = state.get("tone", "Professional").strip()
    purpose = state.get("purpose", "General Text").strip()
    use_case = state.get("use_case", "General Refinement").strip()

    logger.info(f"Selected tone: {tone}")
    logger.info(f"Selected purpose: {purpose}")
    logger.info(f"Selected enterprise use case: {use_case}")
    logger.info(f"Input length: {len(input_text)} characters")

    if not input_text:
        logger.warning("Validation failed: empty input text")

        return {
            "is_valid": False,
            "error_message": "Input text cannot be empty.",
            "final_output": ""
        }

    if len(input_text) > 5000:
        logger.warning("Validation failed: input text too long")

        return {
            "is_valid": False,
            "error_message": "Input text is too long. Please keep it under 5000 characters.",
            "final_output": ""
        }

    if tone not in ALLOWED_TONES:
        logger.warning(f"Validation failed: invalid tone selected - {tone}")

        return {
            "is_valid": False,
            "error_message": f"Invalid tone selected. Allowed tones are: {', '.join(ALLOWED_TONES)}",
            "final_output": ""
        }

    if purpose not in ALLOWED_PURPOSES:
        logger.warning(f"Validation failed: invalid purpose selected - {purpose}")

        return {
            "is_valid": False,
            "error_message": f"Invalid purpose selected. Allowed purposes are: {', '.join(ALLOWED_PURPOSES)}",
            "final_output": ""
        }

    if use_case not in ALLOWED_USE_CASES:
        logger.warning(f"Validation failed: invalid enterprise use case selected - {use_case}")

        return {
            "is_valid": False,
            "error_message": f"Invalid enterprise use case selected. Allowed use cases are: {', '.join(ALLOWED_USE_CASES)}",
            "final_output": ""
        }

    logger.info("Input validation completed successfully")

    return {
        "input_text": input_text,
        "tone": tone,
        "purpose": purpose,
        "use_case": use_case,
        "is_valid": True,
        "error_message": ""
    }
    logger.info("Starting input validation")

    input_text = state.get("input_text", "").strip()
    tone = state.get("tone", "Professional").strip()
    purpose = state.get("purpose", "General Text").strip()
    use_case = state.get("use_case", "General Refinement").strip()

    logger.info(f"Selected tone: {tone}")
    logger.info(f"Selected purpose: {purpose}")
    logger.info(f"Selected enterprise use case: {use_case}")
    logger.info(f"Input length: {len(input_text)} characters")

    if not input_text:
        logger.warning("Validation failed: empty input text")

        return {
            "is_valid": False,
            "error_message": "Input text cannot be empty.",
            "final_output": ""
        }

    if len(input_text) > 5000:
        logger.warning("Validation failed: input text too long")

        return {
            "is_valid": False,
            "error_message": "Input text is too long. Please keep it under 5000 characters.",
            "final_output": ""
        }

    if tone not in ALLOWED_TONES:
        logger.warning(f"Validation failed: invalid tone selected - {tone}")

        return {
            "is_valid": False,
            "error_message": f"Invalid tone selected. Allowed tones are: {', '.join(ALLOWED_TONES)}",
            "final_output": ""
        }

    if purpose not in ALLOWED_PURPOSES:
        logger.warning(f"Validation failed: invalid purpose selected - {purpose}")

        return {
            "is_valid": False,
            "error_message": f"Invalid purpose selected. Allowed purposes are: {', '.join(ALLOWED_PURPOSES)}",
            "final_output": ""
        }

    if use_case not in ALLOWED_USE_CASES:
        logger.warning(f"Validation failed: invalid enterprise use case selected - {use_case}")

        return {
            "is_valid": False,
            "error_message": f"Invalid enterprise use case selected. Allowed use cases are: {', '.join(ALLOWED_USE_CASES)}",
            "final_output": ""
        }

    logger.info("Input validation completed successfully")

    return {
        "input_text": input_text,
        "tone": tone,
        "purpose": purpose,
        "use_case": use_case,
        "is_valid": True,
        "error_message": ""
    }

    logger.info("Starting input validation")

    input_text = state.get("input_text", "").strip()
    tone = state.get("tone", "Professional").strip()
    purpose = state.get("purpose", "General Text").strip()

    logger.info(f"Selected tone: {tone}")
    logger.info(f"Selected purpose: {purpose}")
    logger.info(f"Input length: {len(input_text)} characters")

    if not input_text:
        logger.warning("Validation failed: empty input text")

        return {
            "is_valid": False,
            "error_message": "Input text cannot be empty.",
            "final_output": ""
        }

    if len(input_text) > 5000:
        logger.warning("Validation failed: input text too long")

        return {
            "is_valid": False,
            "error_message": "Input text is too long. Please keep it under 5000 characters.",
            "final_output": ""
        }

    if tone not in ALLOWED_TONES:
        logger.warning(f"Validation failed: invalid tone selected - {tone}")

        return {
            "is_valid": False,
            "error_message": f"Invalid tone selected. Allowed tones are: {', '.join(ALLOWED_TONES)}",
            "final_output": ""
        }

    if purpose not in ALLOWED_PURPOSES:
        logger.warning(f"Validation failed: invalid purpose selected - {purpose}")

        return {
            "is_valid": False,
            "error_message": f"Invalid purpose selected. Allowed purposes are: {', '.join(ALLOWED_PURPOSES)}",
            "final_output": ""
        }

    logger.info("Input validation completed successfully")

    return {
        "input_text": input_text,
        "tone": tone,
        "purpose": purpose,
        "is_valid": True,
        "error_message": ""
    }

    logger.info("Starting input validation")

    input_text = state.get("input_text", "").strip()
    tone = state.get("tone", "Professional").strip()

    logger.info(f"Selected tone: {tone}")
    logger.info(f"Input length: {len(input_text)} characters")

    if not input_text:
        logger.warning("Validation failed: empty input text")

        return {
            "is_valid": False,
            "error_message": "Input text cannot be empty.",
            "final_output": ""
        }

    if len(input_text) > 5000:
        logger.warning("Validation failed: input text too long")

        return {
            "is_valid": False,
            "error_message": "Input text is too long. Please keep it under 5000 characters.",
            "final_output": ""
        }

    if tone not in ALLOWED_TONES:
        logger.warning(f"Validation failed: invalid tone selected - {tone}")

        return {
            "is_valid": False,
            "error_message": f"Invalid tone selected. Allowed tones are: {', '.join(ALLOWED_TONES)}",
            "final_output": ""
        }

    logger.info("Input validation completed successfully")

    return {
        "input_text": input_text,
        "tone": tone,
        "is_valid": True,
        "error_message": ""
    }


def grammar_correction(state):
    if not state.get("is_valid"):
        logger.warning("Skipping grammar correction due to invalid input")
        return {}

    try:
        logger.info("Starting grammar correction node")

        prompt = build_grammar_prompt(state["input_text"])
        corrected_text = call_llm(prompt)

        logger.info("Grammar correction completed successfully")

        return {
            "grammar_fixed_text": corrected_text
        }

    except Exception as e:
        logger.error(f"Grammar correction failed: {str(e)}")

        return {
            "is_valid": False,
            "error_message": f"Grammar correction failed: {str(e)}",
            "final_output": state.get("input_text", "")
        }


def professional_refinement(state):
    if not state.get("is_valid"):
        logger.warning("Skipping professional refinement due to invalid input")
        return {}

    try:
        logger.info("Starting tone, purpose, and enterprise use-case refinement node")

        tone = state.get("tone", "Professional")
        purpose = state.get("purpose", "General Text")
        use_case = state.get("use_case", "General Refinement")
        grammar_fixed_text = state.get("grammar_fixed_text", state["input_text"])

        logger.info(f"Applying tone: {tone}")
        logger.info(f"Applying purpose: {purpose}")
        logger.info(f"Applying enterprise use case: {use_case}")

        prompt = build_refinement_prompt(
            grammar_fixed_text,
            tone,
            purpose,
            use_case
        )

        refined_text = call_llm(prompt)

        logger.info("Tone, purpose, and enterprise use-case refinement completed successfully")

        return {
            "professional_text": refined_text
        }

    except Exception as e:
        logger.error(f"Professional refinement failed: {str(e)}")

        return {
            "is_valid": False,
            "error_message": f"Professional refinement failed: {str(e)}",
            "final_output": state.get("grammar_fixed_text", state.get("input_text", ""))
        }
    if not state.get("is_valid"):
        logger.warning("Skipping professional refinement due to invalid input")
        return {}

    try:
        logger.info("Starting tone and purpose-based refinement node")

        tone = state.get("tone", "Professional")
        purpose = state.get("purpose", "General Text")
        grammar_fixed_text = state.get("grammar_fixed_text", state["input_text"])

        logger.info(f"Applying tone: {tone}")
        logger.info(f"Applying purpose: {purpose}")

        prompt = build_refinement_prompt(grammar_fixed_text, tone, purpose)
        refined_text = call_llm(prompt)

        logger.info("Tone and purpose-based refinement completed successfully")

        return {
            "professional_text": refined_text
        }

    except Exception as e:
        logger.error(f"Professional refinement failed: {str(e)}")

        return {
            "is_valid": False,
            "error_message": f"Professional refinement failed: {str(e)}",
            "final_output": state.get("grammar_fixed_text", state.get("input_text", ""))
        }
    if not state.get("is_valid"):
        logger.warning("Skipping professional refinement due to invalid input")
        return {}

    try:
        logger.info("Starting tone-based refinement node")

        tone = state.get("tone", "Professional")
        grammar_fixed_text = state.get("grammar_fixed_text", state["input_text"])

        logger.info(f"Applying tone: {tone}")

        prompt = build_refinement_prompt(grammar_fixed_text, tone)
        refined_text = call_llm(prompt)

        logger.info("Tone-based refinement completed successfully")

        return {
            "professional_text": refined_text
        }

    except Exception as e:
        logger.error(f"Professional refinement failed: {str(e)}")

        return {
            "is_valid": False,
            "error_message": f"Professional refinement failed: {str(e)}",
            "final_output": state.get("grammar_fixed_text", state.get("input_text", ""))
        }


def final_validation(state):
    logger.info("Starting final validation node")

    if state.get("error_message"):
        logger.warning(f"Final validation completed with error: {state.get('error_message')}")

        return {
            "final_output": state.get("final_output", "")
        }

    final_text = (
        state.get("professional_text")
        or state.get("grammar_fixed_text")
        or state.get("input_text")
        or ""
    ).strip()

    logger.info("Final output generated successfully")

    return {
        "final_output": final_text
    }