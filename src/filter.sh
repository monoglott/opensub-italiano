#!/bin/sh
awk '/^[abcdefghilmnopqrstuvzàèéìíòóùúABCDEFGHILMNOPQRSTUVZÀÈÉÌÍÒÓÙÚ]+$/{ print $0 }' $1
