import dearpygui.dearpygui as dpg
import io
import UnityPy
import sys
import os
from random import randbytes


started = 0;
visColor = []
nonVisColor = []
itemColor = []
item2_color = []

def getColors(shaderLoc,daColor):
    shad = dpg.get_value(daColor);
    r = float(shad[0]/ 255 * 100)/100;
    g = float(shad[1]/ 255 * 100)/100;
    b = float(shad[2]/ 255 * 100)/100;
    a = float(shad[3]/ 255 * 100)/100;

    shaderLoc["m_DefValue[0]"] = r;
    shaderLoc["m_DefValue[1]"] = g;
    shaderLoc["m_DefValue[2]"] = b;
    shaderLoc["m_DefValue[3]"] = a;
    print([r,g,b,a])
    

def editShader():
    src,out = "shaders","whatthefuck2"
    env = UnityPy.load(src)
    for obj in env.objects:
        
        if obj.type.name == "Shader":
            
            if obj.path_id == 8646871023065948827:
                person_shader = obj.read_typetree();

                person_shader["m_ParsedForm"]["m_PropInfo"]["m_Props"][0]["m_Description "] = 1;

                person_shader["m_ParsedForm"]["m_PropInfo"]["m_Props"][0]["m_DefValue[0]"] = 1;
                person_shader["m_ParsedForm"]["m_PropInfo"]["m_Props"][0]["m_DefValue[1]"] = 1;
                person_shader["m_ParsedForm"]["m_PropInfo"]["m_Props"][0]["m_DefValue[2]"] = 1;
                person_shader["m_ParsedForm"]["m_PropInfo"]["m_Props"][0]["m_DefValue[3]"] = 1;


                visible = person_shader["m_ParsedForm"]["m_PropInfo"]["m_Props"][1];
                not_visible = person_shader["m_ParsedForm"]["m_PropInfo"]["m_Props"][2];
                getColors(visible,visColor)
                getColors(not_visible,nonVisColor)
                obj.save_typetree(person_shader)
                print('edited '+str(obj.path_id))


            if obj.path_id == -9098473984068178372 or obj.path_id == 5767049091772583961:
                item_shader = obj.read_typetree();
                item_shader["m_ParsedForm"]["m_PropInfo"]["m_Props"][0]["m_DefValue[0]"] = 1;
                item_shader["m_ParsedForm"]["m_PropInfo"]["m_Props"][0]["m_DefValue[1]"] = 1;
                item_shader["m_ParsedForm"]["m_PropInfo"]["m_Props"][0]["m_DefValue[2]"] = 1;
                item_shader["m_ParsedForm"]["m_PropInfo"]["m_Props"][0]["m_DefValue[3]"] = 1;


                item_p1 = item_shader["m_ParsedForm"]["m_PropInfo"]["m_Props"][1];
                item_p2 = item_shader["m_ParsedForm"]["m_PropInfo"]["m_Props"][2];
                getColors(item_p1,itemColor)
                getColors(item_p2,item2_color)
                obj.save_typetree(item_shader)
                print('edited '+str(obj.path_id))


                
    new_file = env.file.save()
    

    with open(out, 'wb') as f:
        f.write(new_file)
    with open(out, "ab") as f:
        f.write(randbytes(9999999))
    truncate = os.system("truncate.exe "+out+" 62678698")
    print('Finished!')


ppp = dpg.create_viewport()
       

    

with dpg.window(label="Charmy Color Picker - Avalon",autosize=True):
            visColor = dpg.add_color_picker(label="When Visible")
            dpg.add_spacing()
            dpg.add_spacing()
            nonVisColor = dpg.add_color_picker(label="When Not Visible")
            dpg.add_spacing()
            dpg.add_spacing()
            itemColor = dpg.add_color_picker(label="Items")
            dpg.add_spacing()
            dpg.add_spacing()
            item2_color = dpg.add_color_picker(label="Items2?")
            dpg.add_button(label="Save", callback=editShader)
     

dpg.create_viewport(title='Custom Title', width=350, height=800)  # create viewport takes in config options too!


dpg.setup_dearpygui()
dpg.show_viewport(ppp)
dpg.start_dearpygui()

