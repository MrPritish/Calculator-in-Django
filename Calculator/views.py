from django.shortcuts import render , HttpResponse

# Create your views here.
# eq is for equation
eq = ''
# dis is for displaying the eq
dis = ""
# final is for final answer
final = ''
def index(request):
    
    global eq
    global dis
    global final

    if request.GET.get('num1'):
        
        text = request.GET.get('num1' , 'default')
        eq += text
        dis += text
        
    elif request.GET.get('num2'):

        text = request.GET.get('num2' , 'default1')
        eq += text
        dis += text
    
    elif request.GET.get('num3'):

        text = request.GET.get('num3' , 'default1')
        eq += text
        dis += text
    
    elif request.GET.get('num4'):

        text = request.GET.get('num4' , 'default1')
        eq += text
        dis += text
    
    elif request.GET.get('num5'):

        text = request.GET.get('num5' , 'default1')
        eq += text
        dis += text
    
    elif request.GET.get('num6'):

        text = request.GET.get('num6' , 'default1')
        eq += text
        dis += text
    
    elif request.GET.get('num7'):

        text = request.GET.get('num7' , 'default1')
        eq += text
        dis += text
    
    elif request.GET.get('num8'):

        text = request.GET.get('num8' , 'default1')
        eq += text
        dis += text
    
    elif request.GET.get('num9'):

        text = request.GET.get('num9' , 'default1')
        eq += text
        dis += text
    
    elif request.GET.get('num0'):

        text = request.GET.get('num0' , 'default1')
        eq += text
        dis += text
    
    elif request.GET.get('num+'):

        text = request.GET.get('num+' , 'default1')
        eq += text
        dis += text

    
    elif request.GET.get('num-'):

        text = request.GET.get('num-' , 'default1')
        eq += text
        dis += text
    
    elif request.GET.get('num*'):

        text = request.GET.get('num*' , 'default1')
        eq += text
        dis += text

    elif request.GET.get('num/'):

        text = request.GET.get('num/' , 'default1')
        eq += text
        dis += text
    
    elif request.GET.get('num.'):

        text = request.GET.get('num.' , 'default1')
        eq += text
        dis += text

    elif request.GET.get('numx*x'):

        if dis != '' and eq!='':        
            
            dis += f"*{eq}"
            eq += (f"*{eq}")
            final = eval(eq)
            
        
        else:
            final = "please eneter a number first"
    
    elif request.GET.get('num1/x'):

        
        dis = f"1/{eq}"
        eq = f"1/{eq}"
        final = eval(eq)
    
    elif request.GET.get('num-/+'):

        

        final = "this function is under development!!"
    
    elif request.GET.get('num='):

        text = request.GET.get('num=' , 'default1')
        if eq != '' and "=" not in dis :
            
            try:

                final = eval(eq)
                dis += text
                
            
            except:
                final = "please enter proper values"
            
        else :
            
            eq = ''
            
            
        
    else:

        eq = ''
        dis = ''
        final = ''

    

        
    params = {'fin' : final , 'display' : dis }
    
    return render (request , 'index.html' , params)








