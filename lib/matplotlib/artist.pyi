from .axes._base import _AxesBase
from .backend_bases import RendererBase, MouseEvent
from .figure import Figure, SubFigure
from .path import Path
from .patches import Patch
from .patheffects import AbstractPathEffect
from .transforms import (
    Bbox,
    Transform,
    TransformedPatchPath,
    TransformedPath,
)

import numpy as np

from collections.abc import Callable, Iterable
from typing import Any, NamedTuple, TextIO, overload
from numpy.typing import ArrayLike

def allow_rasterization(draw): ...

class _XYPair(NamedTuple):
    x: ArrayLike
    y: ArrayLike

class _Unset: ...

class Artist:
    zorder: float
    def __init_subclass__(cls): ...
    stale_callback: Callable[[Artist, bool], None] | None
    figure: Figure | SubFigure | None
    clipbox: Bbox | None
    def __init__(self) -> None: ...
    def remove(self) -> None: ...
    def have_units(self) -> bool: ...
    # TODO units
    def convert_xunits(self, x): ...
    def convert_yunits(self, y): ...
    @property
    def axes(self) -> _AxesBase | None: ...
    @axes.setter
    def axes(self, new_axes: _AxesBase | None) -> None: ...
    @property
    def stale(self) -> bool: ...
    @stale.setter
    def stale(self, val: bool) -> None: ...
    def get_window_extent(self, renderer: RendererBase | None = ...) -> Bbox: ...
    def get_tightbbox(self, renderer: RendererBase | None = ...) -> Bbox | None: ...
    def add_callback(self, func: Callable[[Artist], Any]) -> int: ...
    def remove_callback(self, oid: int) -> None: ...
    def pchanged(self) -> None: ...
    def is_transform_set(self) -> bool: ...
    def set_transform(self, t: Transform | None) -> None: ...
    def get_transform(self) -> Transform: ...
    def get_children(self) -> list[Artist]: ...
    # TODO can these dicts be type narrowed? e.g. str keys
    def contains(self, mouseevent: MouseEvent) -> tuple[bool, dict[Any, Any]]: ...
    def pickable(self) -> bool: ...
    def pick(self, mouseevent: MouseEvent) -> None: ...
    def set_picker(
        self,
        picker: None
        | bool
        | float
        | Callable[[Artist, MouseEvent], tuple[bool, dict[Any, Any]]],
    ) -> None: ...
    def get_picker(
        self,
    ) -> None | bool | float | Callable[
        [Artist, MouseEvent], tuple[bool, dict[Any, Any]]
    ]: ...
    def get_url(self) -> str | None: ...
    def set_url(self, url: str | None) -> None: ...
    def get_gid(self) -> str | None: ...
    def set_gid(self, gid: str | None) -> None: ...
    def get_snap(self) -> bool | None: ...
    def set_snap(self, snap: bool | None) -> None: ...
    def get_sketch_params(self) -> tuple[float, float, float] | None: ...
    def set_sketch_params(
        self,
        scale: float | None = ...,
        length: float | None = ...,
        randomness: float | None = ...,
    ) -> None: ...
    def set_path_effects(self, path_effects: list[AbstractPathEffect]) -> None: ...
    def get_path_effects(self) -> list[AbstractPathEffect]: ...
    def get_figure(self) -> Figure | None: ...
    def set_figure(self, fig: Figure) -> None: ...
    def set_clip_box(self, clipbox: Bbox | None) -> None: ...
    def set_clip_path(
        self,
        path: Patch | Path | TransformedPath | TransformedPatchPath | None,
        transform: Transform | None = ...,
    ) -> None: ...
    def get_alpha(self) -> float | None: ...
    def get_visible(self) -> bool: ...
    def get_animated(self) -> bool: ...
    def get_in_layout(self) -> bool: ...
    def get_clip_on(self) -> bool: ...
    def get_clip_box(self) -> Bbox | None: ...
    def get_clip_path(
        self,
    ) -> Patch | Path | TransformedPath | TransformedPatchPath | None: ...
    def get_transformed_clip_path_and_affine(
        self,
    ) -> tuple[None, None] | tuple[Path, Transform]: ...
    def set_clip_on(self, b: bool) -> None: ...
    def get_rasterized(self) -> bool: ...
    def set_rasterized(self, rasterized: bool) -> None: ...
    def get_agg_filter(self): ...
    def set_agg_filter(
        self, filter_func: Callable[[ArrayLike, float], tuple[np.ndarray, float, float]]
    ) -> None: ...
    def draw(self, renderer: RendererBase) -> None: ...
    def set_alpha(self, alpha: float | None) -> None: ...
    def set_visible(self, b: bool) -> None: ...
    def set_animated(self, b: bool) -> None: ...
    def set_in_layout(self, in_layout: bool) -> None: ...
    def get_label(self) -> object: ...
    def set_label(self, s: object) -> None: ...
    def get_zorder(self) -> float: ...
    def set_zorder(self, level: float) -> None: ...
    @property
    def sticky_edges(self) -> _XYPair: ...
    def update_from(self, other: Artist) -> None: ...
    def properties(self) -> dict[str, Any]: ...
    def update(self, props: dict[str, Any]) -> Any: ...
    def _internal_update(self, kwargs): ...
    def set(self, **kwargs: Any): ...
    def findobj(
        self,
        match: None | Callable[[Artist], bool] | type[Artist] = ...,
        include_self: bool = ...,
    ) -> list[Artist]: ...
    def get_cursor_data(self, event: MouseEvent) -> Any: ...
    def format_cursor_data(self, data: Any) -> str: ...
    def get_mouseover(self) -> bool: ...
    def set_mouseover(self, mouseover: bool) -> None: ...
    @property
    def mouseover(self) -> bool: ...
    @mouseover.setter
    def mouseover(self, mouseover: bool) -> None: ...

class ArtistInspector:
    oorig: Artist | type[Artist]
    o: type[Artist]
    aliasd: dict[str, set[str]]
    def __init__(
        self, o: Artist | type[Artist] | Iterable[Artist | type[Artist]]
    ) -> None: ...
    def get_aliases(self) -> dict[str, set[str]]: ...
    def get_valid_values(self, attr: str) -> str | None: ...
    def get_setters(self) -> list[str]: ...
    @staticmethod
    def number_of_parameters(func: Callable) -> int: ...
    @staticmethod
    def is_alias(method: Callable) -> bool: ...
    def aliased_name(self, s: str) -> str: ...
    def aliased_name_rest(self, s: str, target: str) -> str: ...
    @overload
    def pprint_setters(
        self, prop: None = ..., leadingspace: int = ...
    ) -> list[str]: ...
    @overload
    def pprint_setters(self, prop: str, leadingspace: int = ...) -> str: ...
    @overload
    def pprint_setters_rest(
        self, prop: None = ..., leadingspace: int = ...
    ) -> list[str]: ...
    @overload
    def pprint_setters_rest(self, prop: str, leadingspace: int = ...) -> str: ...
    def properties(self) -> dict[str, Any]: ...
    def pprint_getters(self) -> list[str]: ...

def getp(obj: Artist, property: str | None = ...) -> Any: ...

get = getp

def setp(obj: Artist, *args, file: TextIO | None = ..., **kwargs): ...
def kwdoc(artist: Artist | type[Artist] | Iterable[Artist | type[Artist]]) -> str: ...
