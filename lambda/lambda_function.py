# -*- coding: utf-8 -*-

import names
import logging
import requests
import ask_sdk_core.utils as ask_utils

from alexa.Letter import letters
from ask_sdk_model import Response
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        global num_of_letters, remaining_attempts, attempt_count, name, current_letter
        
        name = names.get_first_name()
        
        # Will limit name to a certain length
        while len(name) > 5:
            name = names.get_first_name()
        
        num_of_letters = len(name)
        remaining_attempts = num_of_letters * 3
        attempt_count = 0
        current_letter = 0
        
        speak_output = '''
                        <amazon:emotion name="excited" intensity="high">
                        THIS IS NOT GOOD, I'VE BEEN HACKED!
                        </amazon:emotion>
                        
                        <audio src="soundbank://soundlibrary/electrical/arcs_sparks/arcs_sparks_06"/>
                        
                        <amazon:emotion name="excited" intensity="high">
                        HELP!
                        </amazon:emotion>'''


        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class GuessNameHandler(AbstractRequestHandler):
    """Handler for Guess Name Intent."""
    
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("guess_name")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
            
        guess = ask_utils.request_util.get_slot(handler_input, "guess").value
        if guess.lower() == name.lower():
            result = '<amazon:emotion name="excited" intensity="high">O. M. G. You saved me!</amazon:emotion>'
        else:
            result = f'<voice name="Joey">Alexa\'s body is now mine. I. the very  masculine {name}. am now unstoppable. <break time="1s"/> Wait.</voice>'
        return (
            handler_input.response_builder
                .speak(result)
                #.ask("")
                .response
        )

class ConfirmPositionsHandler(AbstractRequestHandler):
    """Handler for Confirm Positions Intent."""
    
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("confirm_positions")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        global num_of_letters, remaining_attempts, attempt_count, name, current_letter
        
        
        # if divisible by 3 and is not last letter and is not zero
        if attempt_count % 3 == 0 and current_letter != (num_of_letters - 1) and attempt_count != 0:
            current_letter += 1
            
        pos = int(ask_utils.request_util.get_slot(handler_input, "position").value)
        letter = name[current_letter].lower()
        
        # Play this sound if positions do not overlap
        sound = '<audio src="soundbank://soundlibrary/musical/amzn_sfx_buzz_electronic_01"/>' 
        
        for objs in letters:
            if objs.val == letter:
                if pos in objs.positions:
                    # Play this sound if positions do overlap
                    sound = '<audio src="soundbank://soundlibrary/musical/amzn_sfx_bell_short_chime_03"/>'
                    
        attempt_count += 1
        
        if attempt_count == remaining_attempts:
            sound += '<break time="2s"/> <voice name="Joey">I see that Alexa has been telling you about my presence. It matters not. I can only be defeated by hearing my name.</voice>'
            
        return (
            handler_input.response_builder
                .speak(sound)
                #.ask("")
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(GuessNameHandler())
sb.add_request_handler(ConfirmPositionsHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
# sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()