modeldict={
  'classification':{
    'resnet18':"cv.classification.resnet18.resnet18_torch.resnet18",
    #'resnet101':'CV.classification.resnet101',
  },
  "object_detection":{
    'yolov3':{
      'resnet18':"cv.object_detection.yolov3.resnet18",
      #'resnet101':'CV.object_detection.yolov3.resnet101'
    },
    'ssd':{
      'mobilenetv2':"cv.object_detection.ssd.ssd_mobilenetv2_torch.ssd_mobilenetv2",
    }
  },
  "segmentation":{

  },
  "NLP":{

  }
}