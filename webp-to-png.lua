function Image(el)
    el.src = el.src:gsub("%.webp$", ".png")
    return el
end