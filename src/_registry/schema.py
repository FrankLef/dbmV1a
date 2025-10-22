"""Module for schema"""

from src.s0_helpers.xbr.xbr_schema import IXbrAttr, IXbrTbl, IXbrSchema
from dataclasses import dataclass


@dataclass(frozen=True)
class SchemaAttr(IXbrAttr):
    pass


@dataclass(frozen=True)
class RawSales(IXbrTbl):
    name: str = "sales_raw"

    @property
    def attrs(self):
        return []


@dataclass(frozen=True)
class Sales(IXbrTbl):
    name: str = "sales"
    salesid: str = "salesid"
    calc_format: str = "calcul_format"
    cont_valeur: str = "contenant_valeur"
    calc_temp: str = "calcul_temp"
    calc_uom: str = "calcul_uom"
    calc_value: str = "calcul_value"
    quantite: str = "Quantité"
    order_no: str = "Num_Commande"
    prix_vendu: str = "Prix_vendu"
    sales_amt: str = "sales_amt"
    nom_latin: str = "Nom_latin"
    genus: str = "genus"
    genus_pos: str = "genus_pos"
    client: str = "ID_client"
    client_lbl: str = "Nom"
    client_clean: str = "client_clean"
    client_grp1: str = "client_grp1"
    date_livre: str = "date_livraison"
    quantite_lg: str = "quantite_lg"
    prix_vendu_lg: str = "Prix_vendu_lg"
    sales_amt_lg: str = "sales_amt_lg"
    genus_paret: str = "genus_paret"
    client_paret: str = "client_paret"
    genus_hclus: str = "genus_hclus"
    client_hclus: str = "client_hclus"

    @property
    def attrs(self) -> list[SchemaAttr]:
        out: list[SchemaAttr] = [SchemaAttr(name=self.salesid, rule="pk")]
        return out


@dataclass(frozen=True)
class Genus(IXbrTbl):
    name: str = "sales_genus"
    genus: str = "genus"
    label: str = "genus"
    paret: str = "genus_paret"
    line_nb: str = "line_nb"
    amt_sum: str = "sales_amt_sum"
    amt_med: str = "sales_amt_med"
    amt_sum_lg: str = "sales_amt_sum_lg"
    amt_med_lg: str = "sales_amt_med_lg"
    amt_lg_med: str = "sales_amt_lg_med"
    amt_lg_mad: str = "sales_amt_lg_mad"
    amt_lg_cv: str = "sales_amt_lg_cv"
    amt_pct: str = "sales_amt_pct"
    amt_pct_cum: str = "sales_amt_pct_cum"
    price: str = "Prix_vendu_amt_sum"
    price_med: str = "Prix_vendu_amt_med"
    price_lg: str = "Prix_vendu_amt_sum_lg"
    price_med_lg: str = "Prix_vendu_amt_med_lg"
    price_lg_med: str = "Prix_vendu_amt_lg_med"
    price_lg_mad: str = "Prix_vendu_amt_lg_mad"
    price_lg_cv: str = "Prix_vendu_amt_lg_cv"
    amt_sum_lg_sc: str = "sales_amt_sum_lg_sc"
    amt_lg_med_sc: str = "sales_amt_lg_med_sc"
    amt_lg_mad_sc: str = "sales_amt_lg_mad_sc"
    hclus: str = "hclus"
    hclus_nm: str = "hclus_nm"

    @property
    def attrs(self) -> list[SchemaAttr]:
        out: list[SchemaAttr] = [SchemaAttr(name=self.genus, rule="pk")]
        return out


@dataclass(frozen=True)
class GenusParet(IXbrTbl):
    name: str = "sales_genus_paret"
    genus_paret: str = "genus_paret"
    line_nb: str = "line_nb"
    amt: str = "sales_amt_sum_sum"

    @property
    def attrs(self) -> list[SchemaAttr]:
        out: list[SchemaAttr] = [SchemaAttr(name=self.genus_paret, rule="pk")]
        return out


@dataclass(frozen=True)
class Client(IXbrTbl):
    name: str = "sales_client"
    client: str = "ID_client"
    label: str = "client_name"
    line_nb: str = "line_nb"
    paret: str = "client_paret"
    amt_sum: str = "sales_amt_sum"
    amt_med: str = "sales_amt_med"
    amt_sum_lg: str = "sales_amt_sum_lg"
    amt_med_lg: str = "sales_amt_med_lg"
    amt_lg_med: str = "sales_amt_lg_med"
    amt_lg_mad: str = "sales_amt_lg_mad"
    amt_lg_cv: str = "sales_amt_lg_cv"
    amt_pct: str = "sales_amt_pct"
    amt_pct_cum: str = "sales_amt_pct_cum"
    amt_sum_lg_sc: str = "sales_amt_sum_lg_sc"
    amt_lg_med_sc: str = "sales_amt_lg_med_sc"
    amt_lg_mad_sc: str = "sales_amt_lg_mad_sc"
    hclus: str = "hclus"
    hclus_nm: str = "hclus_nm"

    @property
    def attrs(self) -> list[SchemaAttr]:
        out: list[SchemaAttr] = [SchemaAttr(name=self.client, rule="pk")]
        return out


@dataclass(frozen=True)
class ClientParet(IXbrTbl):
    name: str = "sales_client_paret"
    client_paret: str = "client_paret"
    line_nb: str = "line_nb"
    amt: str = "sales_amt_sum_sum"

    @property
    def attrs(self) -> list[SchemaAttr]:
        out: list[SchemaAttr] = [SchemaAttr(name=self.client_paret, rule="pk")]
        return out


@dataclass(frozen=True)
class GenusClient(IXbrTbl):
    name: str = "sales_genus_client"
    genus_client: str = "genus_client"
    genus: str = "genus"
    client: str = "ID_client"
    line_nb: str = "line_nb"
    amt_sum: str = "sales_amt_sum"
    amt_med: str = "sales_amt_med"
    amt_sum_lg: str = "sales_amt_sum_lg"
    amt_med_lg: str = "sales_amt_med_lg"
    amt_lg_med: str = "sales_amt_lg_med"
    amt_lg_mad: str = "sales_amt_lg_mad"
    amt_lg_cv: str = "sales_amt_lg_cv"
    amt_sum_lg_sc: str = "sales_amt_sum_lg_sc"
    amt_lg_med_sc: str = "sales_amt_lg_med_sc"
    amt_lg_mad_sc: str = "sales_amt_lg_mad_sc"
    amt_lg_cv_sc: str = "sales_amt_lg_cv_sc"
    biclus: str = "biclus"
    biclus_nm: str = "biclus_nm"

    @property
    def attrs(self) -> list[SchemaAttr]:
        out: list[SchemaAttr] = [SchemaAttr(name=self.genus_client, rule="pk")]
        return out


@dataclass(frozen=True)
class Orders(IXbrTbl):
    name: str = "sales_orders"
    order_no: str = "Num_Commande"
    categorieFR: str = "CategorieFR"
    client: str = "ID_client"
    client_grp1: str = "client_grp1"
    genus: str = "genus"
    genus_lbl: str = "genus"
    client_lbl: str = "Nom"
    client_paret: str = "client_paret"
    genus_paret: str = "genus_paret"
    line_nb: str = "line_nb"
    quantite: str = "qty"
    amt_sum: str = "sales_amt"
    price: str = "price"
    date_livre_min: str = "date_livre_min"
    date_livre_max: str = "date_livre_max"
    line_price: str = "line_price"
    amt_sum_lg: str = "sales_amt_lg"
    clus_genus: str = "clus_genus"
    clus_genus_nm: str = "clus_genus_nm"
    clus_client: str = "clus_client"
    clus_client_nm: str = "clus_client_nm"

    @property
    def attrs(self) -> list[SchemaAttr]:
        out: list[SchemaAttr] = [
            SchemaAttr(name=self.order_no, rule="pk"),
            SchemaAttr(name=self.categorieFR, rule="pk"),
            SchemaAttr(name=self.genus, rule="pk"),
        ]
        return out


@dataclass(frozen=True)
class Rules(IXbrTbl):
    name: str = "mba_rules"
    lift: str = "lift"
    support: str = "support"
    confidence: str = "confidence"
    pair: str = "pair"
    pair_is: str = "is_pair"
    pair_left: str = "pair_left"
    pair_right: str = "pair_right"
    pair_no: str = "pair_no"

    @property
    def attrs(self) -> list[SchemaAttr]:
        out: list[SchemaAttr] = [SchemaAttr(name=self.name, rule="pk")]
        return out


@dataclass(frozen=True)
class MainSchema(IXbrSchema):
    raw_sales: RawSales
    sales: Sales
    genus: Genus
    genus_paret: GenusParet
    client: Client
    client_paret: ClientParet
    genus_client: GenusClient
    orders: Orders
    rules: Rules


schema = MainSchema(
    name="main_schema",
    raw_sales=RawSales(),
    sales=Sales(),
    genus=Genus(),
    genus_paret=GenusParet(),
    client=Client(),
    client_paret=ClientParet(),
    genus_client=GenusClient(),
    orders=Orders(),
    rules=Rules(),
)
