import xml.dom.minidom
import os,shutil
from xml.dom.minidom import parse
import argparse

def parse_args():
    """
    Parse input arguments
    """
    parser = argparse.ArgumentParser(description='Transform PASCAL detection results txts to xmls')
    parser.add_argument('--txt', dest='txt_rootdir', help='PASCAL detection results txts rootdir',
                        default='/home/chong/lzx/oicr/data/VOCdevkit2007/results/VOC2007/Main/', type=str)
    parser.add_argument('--list', dest='voclist_dir',
                        help='The txt of dataset image list, eg: test.txt',
                        default='/home/chong/lzx/oicr/data/VOCdevkit2007/VOC2007/ImageSets/Main/trainval.txt',
                        type=str)
    parser.add_argument('--xml', dest='xml_newdir',
                        help='xml save_dir',
                        default='./annotations_new', type=str)
    parser.add_argument('--ts', dest='xml_tmpdir',
                        help='Temporary storage directory',
                        default='./annotations', type=str)
    args = parser.parse_args()
    return args
def pascal_voc_xml_trans(xml_filename,
	                    folder,
	                    filename,
	                    source_database,
	                    source_annotation,
	                    source_image,
	                    width,
	                    height,
	                    depth,
	                    segmented,
	                    name,
	                    pose,
	                    truncated,
	                    difficult,
	                    xmin,
	                    ymin,
	                    xmax,
	                    ymax):
    # root
    impl = xml.dom.minidom.getDOMImplementation()
    dom = impl.createDocument(None, 'annotation', None)
    node_annotation = dom.documentElement
    # folder
    node_folder = dom.createElement('folder')
    text_folder = dom.createTextNode(folder)
    node_folder.appendChild(text_folder)
    node_annotation.appendChild(node_folder)
    # filename
    node_filename = dom.createElement('filename')
    text_filename=dom.createTextNode(filename)
    node_filename.appendChild(text_filename)
    node_annotation.appendChild(node_filename)
    # source
    node_source=dom.createElement('source')
    node_source_database=dom.createElement('database')
    text_source_database=dom.createTextNode(source_database)
    node_source_database.appendChild(text_source_database)
    node_source_annotation=dom.createElement('annotation')
    text_source_annotation=dom.createTextNode(source_annotation)
    node_source_annotation.appendChild(text_source_annotation)
    node_source_image=dom.createElement('image')
    text_source_image=dom.createTextNode(source_image)
    node_source_image.appendChild(text_source_image)
    node_source.appendChild(node_source_database)
    node_source.appendChild(node_source_annotation)
    node_source.appendChild(node_source_image)
    node_annotation.appendChild(node_source)
    # size
    node_size=dom.createElement('size')
    node_size_width=dom.createElement('width')
    text_size_width=dom.createTextNode(width)
    node_size_width.appendChild(text_size_width)
    node_size_height=dom.createElement('height')
    text_size_height=dom.createTextNode(height)
    node_size_height.appendChild(text_size_height)
    node_size_depth=dom.createElement('depth')
    text_size_depth=dom.createTextNode(depth)
    node_size_depth.appendChild(text_size_depth)
    node_size.appendChild(node_size_width)
    node_size.appendChild(node_size_height)
    node_size.appendChild(node_size_depth)
    node_annotation.appendChild(node_size)
    # segmented
    node_segmented=dom.createElement('segmented')
    text_segmented=dom.createTextNode(segmented)
    node_segmented.appendChild(text_segmented)
    node_annotation.appendChild(node_segmented)
    # object
    node_object=dom.createElement('object')
    node_object_name=dom.createElement('name')
    text_object_name=dom.createTextNode(name)
    node_object_name.appendChild(text_object_name)
    node_object_pose=dom.createElement('pose')
    text_object_pose=dom.createTextNode(pose)
    node_object_pose.appendChild(text_object_pose)
    node_object_truncated=dom.createElement('truncated')
    text_object_truncated=dom.createTextNode(truncated)
    node_object_truncated.appendChild(text_object_truncated)
    node_object_difficult=dom.createElement('difficult')
    text_object_difficult=dom.createTextNode(difficult)
    node_object_difficult.appendChild(text_object_difficult)
    # object-bndbox
    node_object_bndbox=dom.createElement('bndbox')
    node_object_bndbox_xmin=dom.createElement('xmin')
    node_object_bndbox_ymin=dom.createElement('ymin')
    node_object_bndbox_xmax=dom.createElement('xmax')
    node_object_bndbox_ymax=dom.createElement('ymax')
    text_object_bndbox_xmin=dom.createTextNode(xmin)
    text_object_bndbox_ymin=dom.createTextNode(ymin)
    text_object_bndbox_xmax=dom.createTextNode(xmax)
    text_object_bndbox_ymax=dom.createTextNode(ymax)
    node_object_bndbox_xmin.appendChild(text_object_bndbox_xmin)
    node_object_bndbox_ymin.appendChild(text_object_bndbox_ymin)
    node_object_bndbox_xmax.appendChild(text_object_bndbox_xmax)
    node_object_bndbox_ymax.appendChild(text_object_bndbox_ymax)
    node_object_bndbox.appendChild(node_object_bndbox_xmin)
    node_object_bndbox.appendChild(node_object_bndbox_ymin)
    node_object_bndbox.appendChild(node_object_bndbox_xmax)
    node_object_bndbox.appendChild(node_object_bndbox_ymax)
    node_object.appendChild(node_object_name)
    node_object.appendChild(node_object_pose)
    node_object.appendChild(node_object_truncated)
    node_object.appendChild(node_object_difficult)
    node_object.appendChild(node_object_bndbox)
    node_annotation.appendChild(node_object)
    pascal_voc_xml=open(xml_filename,'w')
    content=node_annotation.toprettyxml()
    pascal_voc_xml.writelines(content)
    pascal_voc_xml.close()


def add_bndbox_node(xml_filename,
	                name,
	                xmin,
	                ymin,
	                xmax,
	                ymax,
	                pose='Unspecified',
	                truncated='0',
	                difficult='0',
):
    #dom = xml.dom.minidom.parse(xml_filename) 
    #node_annotation = dom.documentElement
    dom,node_annotation = load_xml(xml_filename)
    node_object=dom.createElement('object')
    node_object_name=dom.createElement('name')
    text_object_name=dom.createTextNode(name)
    node_object_name.appendChild(text_object_name)
    node_object_pose=dom.createElement('pose')
    text_object_pose=dom.createTextNode(pose)
    node_object_pose.appendChild(text_object_pose)
    node_object_truncated=dom.createElement('truncated')
    text_object_truncated=dom.createTextNode(truncated)
    node_object_truncated.appendChild(text_object_truncated)
    node_object_difficult=dom.createElement('difficult')
    text_object_difficult=dom.createTextNode(difficult)
    node_object_difficult.appendChild(text_object_difficult)
    # object-bndbox
    node_object_bndbox=dom.createElement('bndbox')
    node_object_bndbox_xmin=dom.createElement('xmin')
    node_object_bndbox_ymin=dom.createElement('ymin')
    node_object_bndbox_xmax=dom.createElement('xmax')
    node_object_bndbox_ymax=dom.createElement('ymax')
    text_object_bndbox_xmin=dom.createTextNode(xmin)
    text_object_bndbox_ymin=dom.createTextNode(ymin)
    text_object_bndbox_xmax=dom.createTextNode(xmax)
    text_object_bndbox_ymax=dom.createTextNode(ymax)
    node_object_bndbox_xmin.appendChild(text_object_bndbox_xmin)
    node_object_bndbox_ymin.appendChild(text_object_bndbox_ymin)
    node_object_bndbox_xmax.appendChild(text_object_bndbox_xmax)
    node_object_bndbox_ymax.appendChild(text_object_bndbox_ymax)
    node_object_bndbox.appendChild(node_object_bndbox_xmin)
    node_object_bndbox.appendChild(node_object_bndbox_ymin)
    node_object_bndbox.appendChild(node_object_bndbox_xmax)
    node_object_bndbox.appendChild(node_object_bndbox_ymax)
    node_object.appendChild(node_object_name)
    node_object.appendChild(node_object_pose)
    node_object.appendChild(node_object_truncated)
    node_object.appendChild(node_object_difficult)
    node_object.appendChild(node_object_bndbox)
    node_annotation.appendChild(node_object)
    pascal_voc_xml=open(xml_filename,'w')
    content=node_annotation.toprettyxml()
    pascal_voc_xml.writelines(content)
    pascal_voc_xml.close()
def add_blank_xml(xml_filename,
	            folder,
	            filename,
	            source_database,
	            source_annotation,
	            source_image,
	            width,
	            height,
	            depth,
	            segmented
	            ):
    # root
    impl = xml.dom.minidom.getDOMImplementation()
    dom = impl.createDocument(None, 'annotation', None)
    node_annotation = dom.documentElement
    # folder
    node_folder = dom.createElement('folder')
    text_folder = dom.createTextNode(folder)
    node_folder.appendChild(text_folder)
    node_annotation.appendChild(node_folder)
    # filename
    node_filename = dom.createElement('filename')
    text_filename=dom.createTextNode(filename)
    node_filename.appendChild(text_filename)
    node_annotation.appendChild(node_filename)
    # source
    node_source=dom.createElement('source')
    node_source_database=dom.createElement('database')
    text_source_database=dom.createTextNode(source_database)
    node_source_database.appendChild(text_source_database)
    node_source_annotation=dom.createElement('annotation')
    text_source_annotation=dom.createTextNode(source_annotation)
    node_source_annotation.appendChild(text_source_annotation)
    node_source_image=dom.createElement('image')
    text_source_image=dom.createTextNode(source_image)
    node_source_image.appendChild(text_source_image)
    node_source.appendChild(node_source_database)
    node_source.appendChild(node_source_annotation)
    node_source.appendChild(node_source_image)
    node_annotation.appendChild(node_source)
    # size
    node_size=dom.createElement('size')
    node_size_width=dom.createElement('width')
    text_size_width=dom.createTextNode(width)
    node_size_width.appendChild(text_size_width)
    node_size_height=dom.createElement('height')
    text_size_height=dom.createTextNode(height)
    node_size_height.appendChild(text_size_height)
    node_size_depth=dom.createElement('depth')
    text_size_depth=dom.createTextNode(depth)
    node_size_depth.appendChild(text_size_depth)
    node_size.appendChild(node_size_width)
    node_size.appendChild(node_size_height)
    node_size.appendChild(node_size_depth)
    node_annotation.appendChild(node_size)
    # segmented
    node_segmented=dom.createElement('segmented')
    text_segmented=dom.createTextNode(segmented)
    node_segmented.appendChild(text_segmented)
    node_annotation.appendChild(node_segmented)
    pascal_voc_xml=open(xml_filename,'w')
    content=node_annotation.toprettyxml()
    pascal_voc_xml.writelines(content)
    pascal_voc_xml.close()


def load_xml(xml_filename):
    dom = xml.dom.minidom.parse(xml_filename)
    root = dom.documentElement              
    return dom,root

def delblank(annotations_file,annotations_newfile):
    xml_list = os.listdir(annotations_file)
    for xml_name in xml_list:
        xml_dir = os.path.join(annotations_file,xml_name)
        xml_newdir = os.path.join(annotations_newfile,xml_name)
        with open(xml_dir,"r") as xml:
            xml_lines = xml.readlines()
            for xml_line in xml_lines:
                f = open(xml_newdir, "a")
                if len(xml_line.strip()) != 0:
                    f.write(xml_line)

def txt2xml(txt_filename,xml_dir):
    class_name = txt_filename.split('_')[-1].split('.')[-2]
    gts=open(txt_filename,'r')
    bboxes=gts.readlines()
    gts.close()
    for bbox in bboxes:
        bbox=bbox.split()
        if float(bbox[1]) > 0.5:
            filename=bbox[0]
            xmin=str(int(float(bbox[2])))
            ymin=str(int(float(bbox[3])))
            xmax=str(int(float(bbox[4])))
            ymax=str(int(float(bbox[5])))
            width='1280'
            height='960'
            depth='3'
            xml_filename = os.path.join(xml_dir, filename.split('.')[0]+'.xml')
            if not os.path.exists(xml_filename):
                pascal_voc_xml_trans(\
                    xml_filename,\
                    'VOC2007',\
                    filename,\
                    'The VOC2007 OICR Database',\
                    'PASCAL VOC2007 OICR',\
                    'OICR',\
                    width,\
                    height,\
                    depth,\
                    '0',\
                    class_name,\
                    'Unspecified',\
                    '0',\
                    '0',\
                    xmin,\
                    ymin,\
                    xmax,\
                    ymax
                    )
            else:
                add_bndbox_node(xml_filename, class_name, xmin, ymin, xmax, ymax)


def add_none_object_xml(xml_dir,voclist_dir):
    width = '1280'
    height = '960'
    depth = '3'
    with open(voclist_dir,'r') as f:
        imagenames = f.readlines()
        for imagename in imagenames:
            image_name = imagename.split('\n')[0]
            xml_file = os.path.join(xml_dir,image_name + '.xml')
            if not os.path.exists(xml_file):
                print(xml_file + 'not exists')
                add_blank_xml(\
                    xml_file,\
                    'VOC2007',\
                    image_name,\
                    'The VOC2007 OICR Database',\
                    'PASCAL VOC2007 OICR',\
                    'OICR_none_object',\
                    width,\
                    height,\
                    depth,\
                    '0'
                    )
                print(xml_file + ' added')

def converter(txt_rootdir, voclist_dir, xml_newdir,xml_tmpdir):
    txt_names  = os.listdir(txt_rootdir)
    print('Creating tmpdir and savedir...')
    if not os.path.exists(xml_tmpdir):
        os.makedirs(xml_tmpdir)
    if not os.path.exists(xml_newdir):
        os.makedirs(xml_newdir)
    for txt_name in txt_names:
        txt_filename = os.path.join(txt_rootdir,txt_name)
        txt2xml(txt_filename,xml_tmpdir)
        print('prossing...' + txt_name)
    print('XML_Analysis Finished,delete blank lines...')
    delblank(xml_tmpdir, xml_newdir)
    print('Deleting blank lines finished,add none-object xmls ...')
    add_none_object_xml(xml_newdir,voclist_dir)
    print('Deleting tmpdir...')
    shutil.rmtree(xml_tmpdir)
    print('finished')

if __name__ == '__main__':
    args = parse_args()
    converter(args.txt_rootdir, args.voclist_dir, args.xml_newdir, args.xml_tmpdir)

