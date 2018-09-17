import config

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from os.path import basename

import coremltools
from keras.utils.generic_utils import get_custom_objects
import tensorflow as tf
from loss import softmax_cross_entropy_with_logits
from keras import losses
from keras.models import load_model
import keras

def send_mail(send_from, subject, text, send_to, files= None):

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = ', '.join(send_to)  
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as fil: 
            ext = f.split('.')[-1:]
            attachedfile = MIMEApplication(fil.read(), _subtype = ext)
            attachedfile.add_header(
                'content-disposition', 'attachment', filename=basename(f) )
        msg.attach(attachedfile)


    smtp = smtplib.SMTP(host="smtp.gmail.com", port= 587) 
    smtp.starttls()
    smtp.login(config.GMAIL_ACCOUNT,config.GMAIL_PASSWORD)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()

def convert_to_coreML(model_path, model_version):
    model = load_model(model_path, custom_objects={'softmax_cross_entropy_with_logits': softmax_cross_entropy_with_logits, 'relu6': keras.applications.mobilenet.relu6, 'DepthwiseConv2D': keras.applications.mobilenet.DepthwiseConv2D})
    coreml_mnist = coremltools.converters.keras.convert(model, add_custom_layers=True)
    coreml_mnist.author = config.CREATOR_NAME
    coreml_mnist.license = config.CREATOR_LICENSE
    coreml_mnist.short_description = config.MODEL_DESCRIPTION
    coreml_mnist.input_description['input1'] = config.MODEL_INPUT_DESCRIPTION
    coreml_mnist.output_description['output1'] = config.MODEL_OUTPUT_DESCRIPTION
    coreml_mnist.save('/run/models/connect4_model' + model_version + '.mlmodel')
