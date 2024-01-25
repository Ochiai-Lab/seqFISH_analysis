import os
import bigfish
import bigfish.stack as stack
import bigfish.detection as detection
import bigfish.multistack as multistack
import bigfish.plot as plot
import numpy as np
import pandas as pd
    
def intensity_calc(fov, geneID_list, summary_data_fid7, ref_data, dir) :
    Pos_no = 'Pos'+str(fov).zfill(2)
    # 細胞核segmentation画像
    path = os.path.join(dir, "1_processed_images", "4_segmentation",  Pos_no, "02_nuc_seg_human_corrected.tif")
    nuc_seg  = stack.read_image(path)
    nuc_seg = nuc_seg.astype('uint16')

    # maskを作る。
    nuc_seg_mask = np.where(nuc_seg > 0, 1, 0)
    
    _df2 = pd.DataFrame()
    
    for geneID in geneID_list:     
        print('fov :' + str(fov) + ', geneID : ' + str(geneID))
        _df1 = summary_data_fid7.loc[(summary_data_fid7['fov'] == fov)&(summary_data_fid7['geneID'] == geneID), :].copy()
        _df1['Stack_ID'] = ref_data.loc[ref_data['geneID']==geneID,'Stack_ID'].values[0]

        file_name = ref_data.loc[ref_data['geneID']==geneID,'Stack_ID'].values[0]+'.tif'

        path_input = os.path.join(dir, "1_processed_images", "3_diveded_files")
        
        path = os.path.join(path_input, Pos_no, file_name)
        # smFISHの画像を選択する。
        dna  = stack.read_image(path)

        dna_masked = dna * nuc_seg_mask
        dna_masked = dna_masked.astype('uint16')


        data_df_spots = _df1.loc[:,['z','y','x']]
        data_df_spots = data_df_spots.rename(columns={'z' : 'Z_pix',
                                                      'y' : 'Y_pix',
                                                      'x' : 'X_pix'})

        data_df_spots

        # DNA-seqFISH画像から輝度値を抽出する際に参照するために、画像をgauss filterする
        dna_gauss = bigfish.stack.gaussian_filter(dna, sigma=1, allow_negative=False)
        dna_gauss_masked = dna_gauss * nuc_seg_mask


        b = data_df_spots.loc[:,"Z_pix":"X_pix"].copy()
        # numpyデータに変換
        b_np = b.to_numpy()
        # 座標を整数に変換
        coords_int_b = np.round(b_np).astype(int)

        coords_int_b
        # ここで、(68, 998, 969)の範囲外になるものが出てくることがあるようだ。
        coords_int_b_t = coords_int_b.T
        coords_int_b_t[0] = np.where(coords_int_b_t[0] > dna.shape[0]-1, dna.shape[0]-1, coords_int_b_t[0])
        coords_int_b_t[0] = np.where(coords_int_b_t[0] < 0, 0, coords_int_b_t[0])
        coords_int_b_t[1] = np.where(coords_int_b_t[1] > dna.shape[1]-1, dna.shape[1]-1, coords_int_b_t[1])
        coords_int_b_t[1] = np.where(coords_int_b_t[1] < 0, 0, coords_int_b_t[1])
        coords_int_b_t[2] = np.where(coords_int_b_t[2] > dna.shape[2]-1, dna.shape[2]-1, coords_int_b_t[2])
        coords_int_b_t[2] = np.where(coords_int_b_t[2] < 0, 0, coords_int_b_t[2])

        coords_int_b = coords_int_b_t.T
        coords_int_b
        # gauss処理したデータの中で、輝点座標の場所の輝度値を抽出
        values_at_coords_b = dna_gauss[tuple(coords_int_b.T)]
        #輝度値をintensity列に代入
        _df1['spot_intensity'] = values_at_coords_b.copy()
        _df1['norm_spot_intensity'] = values_at_coords_b.copy()/np.median(dna_gauss_masked[dna_gauss_masked>0])
        _df2 = pd.concat([_df2, _df1])
        
        # まとめ用のdata_df_spots2にデータを追加
        #summary_data_fid8_int = pd.concat([summary_data_fid8_int, _df1]).copy()
    return _df2
    




def xyz(cell, res_all_red, list_hyb):
    print(cell)
    _df0 = res_all_red[cell][0]
    _df0['hyb_comp'] = ''
    _df0['x_hat_nei'] = ''
    _df0['y_hat_nei'] = ''
    _df0['z_hat_nei'] = ''

    for hyb in range(len(list_hyb)-1):
        if (sum(_df0['hyb']==list_hyb[hyb])>0) and (sum(_df0['hyb']==list_hyb[hyb+1])>0):
            _df0.loc[_df0['hyb']==list_hyb[hyb],'hyb_comp'] = list_hyb[hyb+1]
            _df0.loc[_df0['hyb']==list_hyb[hyb],'x_hat_nei'] = _df0.loc[_df0['hyb']==list_hyb[hyb+1],'x_hat']
            _df0.loc[_df0['hyb']==list_hyb[hyb],'y_hat_nei'] = _df0.loc[_df0['hyb']==list_hyb[hyb+1],'y_hat']
            _df0.loc[_df0['hyb']==list_hyb[hyb],'z_hat_nei'] = _df0.loc[_df0['hyb']==list_hyb[hyb+1],'z_hat']
        return _df1