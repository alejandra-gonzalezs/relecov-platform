import json
import dash_core_components as dcc
import dash_html_components as html
from django_plotly_dash import DjangoDash
from dash.dependencies import Input, Output
import urllib.request as urlreq
import dash_bio as dashbio


def parse_csv(file_path):
    """
    fields => SAMPLE(0), CHROM(1), POS(2), REF(3), ALT(4),
    FILTER(5), DP(6),  REF_DP(7), ALT_DP(8), AF(9), GENE(10),
    EFFECT(11), HGVS_C(12), HGVS_P(13), HGVS_P1LETTER(14),
    CALLER(15), LINEAGE(16)
    """
    # data_array = []  # one field per position
    # headers = []

    # variant_data = []
    # variant_fields = ["pos", "ref", "alt", "dp", "ref_dp", "alt_dp", "af"]
    # variant_pos = [2, 3, 4, 6, 7, 8, 9]

    # effect_fields = ["effect", "hgvs_c", "hgvs_p", "hgvs_p_1_letter"]
    # effect_pos = [11, 12, 13, 14]

    with open(file_path) as fh:
        lines = fh.readlines()

    # headers = lines[0].split(",")

    """
        data_dict = {"variant_dict": {}, "effect_dict": {}}
        for iv in range(len(variant_fields)):
            data_dict["variant_dict"][variant_fields[iv]] = data_array[variant_pos[iv]]
        # effect_dict = {}
        for ix in range(len(effect_fields)):
            data_dict["effect_dict"][effect_fields[ix]] = data_array[effect_pos[ix]]
        data_dict["filter"] = data_array[5]
        data_dict["chromosome"] = data_array[1]
        data_dict["sample"] = data_array[0]
        data_dict["caller"] = data_array[15]
        data_dict["lineage_dict"] = {"lineage": data_array[16], "week": data_array[17]}
        data_dict["gene"] = data_array[10]
        variant_data.append(data_dict)
    """
    return lines


def set_dataframe_needle_plot(lines_from_long_table):  # , sample
    """
    This function receives a python dictionary, a list of selected fields and sets a dataframe from fields_selected_list to represent the graph
    dataframe structure(dict) { x: [], y: [], domains: [], mutationGroups: [],}
    """
    pos_list = []
    af_list = []
    effect_list = []
    gene_list = []
    sample = 214821
    df = {}

    for line in lines_from_long_table[1:]:
        data_array = line.split(",")
        if data_array[0] is sample:
            pos_list.append(data_array[2])
            af_list.append(data_array[9])
            effect_list.append(data_array[11])
            gene_list.append(data_array[10])
    len()
    df["x"] = pos_list
    df["y"] = af_list
    df["domains"] = [
        {"name": "PI3K_p85B", "coord": "32-107"},
        {"name": "PI3K_rbd", "coord": "173-292"},
        {"name": "PI3K_C2", "coord": "350-485"},
        {"name": "PI3Ka", "coord": "519-704"},
        {"name": "PI3_PI4_kinase", "coord": "796-1015"},
    ]
    df["mutationGroups"] = effect_list

    return df


def parse_json_file(json_file):
    """
    This function loads a json file and returns a python dictionary.
    """
    json_parsed = {}
    f = open(json_file)
    json_parsed["data"] = json.load(f)

    return json_parsed


def get_list_of_keys(json_parsed):
    list_of_keys = list(json_parsed["data"].keys())
    return list_of_keys


def create_graphic(data_frame):
    """
    This function represents a graph from a dataframe
    """
    # data = parse_json_file()
    # dataframe = set_dataframe()
    pass


def create_needle_plot_graph():
    app = DjangoDash("needle_plot")

    data = urlreq.urlopen("https://git.io/needle_PIK3CA.json").read().decode("utf-8")

    mdata = json.loads(data)
    # mdata = df

    app.layout = html.Div(
        children=[
            "Show or hide range slider",
            dcc.Dropdown(
                id="default-needleplot-rangeslider",
                options=[{"label": "Show", "value": 1}, {"label": "Hide", "value": 0}],
                clearable=False,
                multi=False,
                value=0,
                style={"width": "400px"},
            ),
            html.Div(
                children=dashbio.NeedlePlot(
                    width="auto", id="dashbio-default-needleplot", mutationData=mdata
                ),
            ),
        ],
    )

    @app.callback(
        Output("dashbio-default-needleplot", "rangeSlider"),
        Input("default-needleplot-rangeslider", "value"),
    )
    def update_needleplot(show_rangeslider):
        return True if show_rangeslider else False
