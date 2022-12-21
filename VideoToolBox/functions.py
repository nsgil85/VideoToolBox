from datetime import datetime
import numpy as np


def show_img(img:np.ndarray):
    cv2.namedWindow('window',cv2.WINDOW_NORMAL)
    cv2.imshow('window',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def load_video(path:str, save_dir:str = None, resize:float = None, length:int=-1): # N x H x W x C
    vidcap = cv2.VideoCapture(path)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    success,image = vidcap.read()
    print(image.shape)
    height, width, layers = image.shape
    if resize is None:
        size = (width,height)
    elif type(resize) is int:
        size = (width//resize,height//resize)
    else:
        size = resize
    count = 0
    frames = []
    while success:  
        if resize is not None:
            image = cv2.resize(image, size, interpolation = cv2.INTER_LINEAR)
        if save_dir != None:
            path = os.path.join(save_dir, "frame_" + str(count).zfill(4) + ".png")
            cv2.imwrite(path, image) 
        frames.append(image)
        success,image = vidcap.read()
        count += 1
        if length > 0 and count >= length:
            break
    print("Video length: ", len(frames))
    return frames, fps, size

    
def save_video(path:str, frame_array:np.ndarray, fps:int, size, losses=None, frame_number:bool=False, writer=None):
    if writer is None:
        if path[-3:] == "mp4":
            out = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
        else:
            out = cv2.VideoWriter(path, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, size)
    else:
        out = writer
    for i in range(len(frame_array)):
        # writing to a image array
        if frame_number:
            frame_array[i] = draw_number(np.asarray(frame_array[i]), i)
        if losses is not None:
            frame_array[i] = draw_number(np.asarray(frame_array[i]), losses[i], x=900, message="Loss: ")
        out.write(frame_array[i])
    if writer is None:
        out.release()

def draw_number(frame:np.ndarray, num:int, x=:int 10, y=:int 10, message:str ="Frame: "):
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("./data/arial.ttf", 45)

    message = message + str(num)
    color = 'rgb(0, 0, 0)'  # black color

    draw.text((x, y), message, fill=color, font=font)
    return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    

def report(msg:str):
    _time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    print(f"{_time}: {msg}")

