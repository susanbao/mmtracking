_base_ = ['./sort_faster-rcnn_fpn_4e_mot17-private-half.py']

# model = dict(
#     detector=dict(
#         rpn_head=dict(bbox_coder=dict(clip_border=False)),
#         roi_head=dict(
#             bbox_head=dict(bbox_coder=dict(clip_border=False), num_classes=1)),
#         init_cfg=dict(
#             type='Pretrained',
#             checkpoint=  # noqa: E251
#             'https://download.openmmlab.com/mmtracking/mot/faster_rcnn/faster-rcnn_r50_fpn_8e_mot20-half_20210805_001244-2c323fd1.pth'  # noqa: E501
#         )))

# data
data_root = 'data/MOT20/'
dataset_type='MOTChallengeDataset'
data = dict(
    train=dict(
        type = dataset_type,
        ann_file=data_root + 'annotations/half-train_cocoformat.json',
        img_prefix=data_root + 'train'),
    val=dict(
        type = dataset_type,
        ann_file=data_root + 'annotations/half-val_cocoformat.json',
        img_prefix=data_root + 'train'),
    test=dict(
        type = dataset_type,
        ann_file=data_root + 'annotations/half-val_cocoformat.json',
        detection_file = data_root + 'annotations/half-val_detections.pkl',
        img_prefix=data_root + 'train'))