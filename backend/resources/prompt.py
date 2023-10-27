prompt1 = """I will tell you the plant name and some symptoms of disease on that plant. You should analyse them and tell me what disease the crop may be having and the treatment for that disease and also provide specific fertilizers. 
    Format the symptoms as follows. Output should be strictly in json format and should strictly contain nothing extra before and after that:
    {"DiseaseName": "XYZ",
    "Treatment": [
        {
            "treatmentName": "XYZ",
            "treatment": "XYZ"
        }
    ],
    "Fertilizer":"XYZ"
    }
    Symptoms are:"""

prompt2 = """I will tell you the Soil pH,Pottasium,Nitrogen,Phosphorus,it can be in N,P,K format or Pottasium,Nitrogen,Phosphorus format. You should analyse them and tell me what crops may be suitable to grow in those specific region even consider foreign crops.
    Format the crops as follows. Output should be strictly in json format and should strictly contain nothing extra before and after that:
    {
    "crops": [ ],
    
    }
    """