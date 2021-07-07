Loss functions:

  Focal loss: Extremely high weight attributed to fringe cases (eg: Plag check).</br>
  Weighted loss: Re-weighting by effective number of samples; lower weight to duplicates
  
Evaluation metics in object detection:
  
  IOU= Ar(Union)/Ar(intersection)</br>
  Higher the value, better the algorithm.</br>
  Average Precision and Mean Average Precision(AP, MAP):</br>
  Summarises the weighted mean of precisions for each threshold with the increase in recall. Mean over all objects for MAP.</br>
  
Normalisation:
  
   Standardising the input(batch/layer).</br>
   Reduces computational time and power.</br>
   Reduces generalization error.</br>
   
Activation functions:

  Rectifies the output to make it lie in a certain range or constrain it to certain values.</br>
  Example: Sigmoid, ReLU, SeLU, eLU, Softmax, etc.</br>
  Different activation functions are appropriate for classification/regression.
  
Convolutional layer:

  Generates a single value for a pixel/element depending on a patch of its neighbourhood.</br>
  Not fully connected.</br>
  
Pooling layer:

  Added after a convolutional layer.</br>
  2 types, average and max pooling.</br>
  
Bounding Box regression:

Popular technique to refine or
predict localization boxes in recent object detection approaches.
 


  
  
  
  
   
  
  
