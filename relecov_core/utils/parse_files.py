def parse_csv_into_list_of_dicts(file_path):
    data_array = []#one field per position
    variant_dict = {}
    variant_list = []
    effect_dict = {}
    effect_list = []
    filter_dict = {}
    filter_list = []
    chromosome_dict = {}
    chromosome_list = []
    sample_dict = {}
    sample_list = []
    caller_dict = {}
    caller_list = []
    lineage_dict = {}
    lineage_list = []
    gene_dict = {}
    gene_list = []
    
    #fields => SAMPLE(0), CHROM(1), POS(2), REF(3), ALT(4), FILTER(5), DP(6),  REF_DP(7), ALT_DP(8), AF(9), GENE(10), EFFECT(11), HGVS_C(12), 
    #   HGVS_P(13), HGVS_P1LETTER(14), CALLER(15), LINEAGE(16)
    with open(file_path) as fh:
        lines = fh.readlines()
    for line in lines[1:]:
        data_array = line.split(",")
        #variant_dict
        variant_dict["pos"] =data_array[2]
        variant_dict["ref"] =data_array[3]
        variant_dict["alt"] =data_array[4]
        variant_dict["dp"] =data_array[6]
        variant_dict["ref_dp"] =data_array[7]
        variant_dict["alt_dp"] =data_array[8]
        variant_dict["af"] =data_array[9]
        variant_dict_copy = variant_dict.copy()
        
        variant_list.append(variant_dict_copy)
        #effect _dict
        effect_dict["effect"] = data_array[11]
        effect_dict["hgvs_c"] = data_array[12]
        effect_dict["hgvs_p"] = data_array[13]
        effect_dict["hgvs_p_1_letter"] = data_array[14]
        effect_dict_copy = effect_dict.copy()
        effect_list.append(effect_dict_copy)
        #filter
        filter_dict["filter"] = data_array[5]
        filter_dict_copy = filter_dict.copy()
        filter_list.append(filter_dict_copy)
        #chromosome
        chromosome_dict["chromosome"] = data_array[1]
        chromosome_dict_copy = chromosome_dict.copy()
        chromosome_list.append(chromosome_dict_copy)
        #sample
        sample_dict["sample"] = data_array[0]
        sample_dict_copy = sample_dict.copy()
        sample_list.append(sample_dict_copy)
        #caller
        caller_dict["caller"] = data_array[15]
        caller_dict_copy = caller_dict.copy()
        caller_list.append(caller_dict_copy)
        #lineage
        lineage_dict["lineage"] = data_array[16]
        lineage_dict["week"] = data_array[17]
        lineage_dict_copy = lineage_dict.copy()
        lineage_list.append(lineage_dict_copy)
        #gene
        gene_dict["gene"] = data_array[10]
        gene_dict_copy = gene_dict.copy()
        gene_list.append(gene_dict_copy)
        
        
    