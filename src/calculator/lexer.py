"""A simple lexical analyzer."""

# Standard library
from collections import namedtuple
from enum import Enum

# Project library
from calculator.token import Token, TokenType

#---------------------------------------------------------------------------------

class Lexer:
    """A simple lexical analyzer."""

    def get_number(self, text, pos):
        """Extract number from text starting at pos."""
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos

        if not text[pos].isdigit():
            return Token(TokenType.ERROR, lexeme), pos

        while pos < length and text[pos].isdigit():
            lexeme += text[pos]
            pos += 1

        return Token(TokenType.NUMBER, lexeme), pos

    def get_add_op(self, text, pos):
        """Extract an addition or subtraction operator."""
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos

        if text[pos] in ['+', '-']:
            lexeme = text[pos]
            pos += 1
            return Token(TokenType.ADD_OP, lexeme), pos
        else:
            return Token(TokenType.ERROR, lexeme), pos

    def get_mul_op(self, text, pos):
        """Extract a multiplication or division operator."""
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos

        if text[pos] in ['*', '/']:
            lexeme = text[pos]
            pos += 1
            return Token(TokenType.MUL_OP, lexeme), pos
        else:
            return Token(TokenType.ERROR, lexeme), pos

    def get_power_op(self, text, pos):
        """Extract a power operator (^)."""
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos

        if text[pos] == '^':
            lexeme = text[pos]
            pos += 1
            return Token(TokenType.POWER_OP, lexeme), pos
        else:
            return Token(TokenType.ERROR, lexeme), pos

    def get_fac_op(self, text, pos):
        """Extract a factorial operator (!)."""
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos

        if text[pos] == '!':
            lexeme = text[pos]
            pos += 1
            return Token(TokenType.FAC_OP, lexeme), pos
        else:
            return Token(TokenType.ERROR, lexeme), pos

    def get_left_paren(self, text, pos):
        """Extract a left parenthesis."""
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos

        if text[pos] == '(':
            lexeme = text[pos]
            pos += 1
            return Token(TokenType.LEFT_PAREN, lexeme), pos
        else:
            return Token(TokenType.ERROR, lexeme), pos

    def get_right_paren(self, text, pos):
        """Extract a right parenthesis."""
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos

        if text[pos] == ')':
            lexeme = text[pos]
            pos += 1
            return Token(TokenType.RIGHT_PAREN, lexeme), pos
        else:
            return Token(TokenType.ERROR, lexeme), pos