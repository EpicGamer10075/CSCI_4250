---------------------------------------|
--- Imports
--
---------------------------------------|

require "controller"


---------------------------------------|
--- Local
--
---------------------------------------|

---
--
function love.update(dt)  
  updateControllers(dt)
  
  updateControllersDebug(dt)
end

---
--
function love.draw()

  drawControllersDebug()  
end
