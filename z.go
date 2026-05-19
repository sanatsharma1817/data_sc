package main
import (
	"encoding/json"
	"net/http"
	"strconv"
	"github.com/gin-gonic/gin"
)
type User struct {
	ID    int    `json:"id"`
	Name  string `json:"name"`
	Email string `json:"email"`
}
var users = []User{
	{ID: 1, Name: "sanat", Email: " "},
	{ID: 2, Name: "rahul", Email: " "},
}
func getUsers(c *gin.Context) {
	c.JSON(http.StatusOK, users)
}
func getUser(c *gin.Context) {
	id, _ := strconv.Atoi(c.Param("id"))
	for _, user := range users {
		if user.ID == id {
			c.JSON(http.StatusOK, user)
			return
		}
	}
	c.JSON(http.StatusNotFound, gin.H{
		"message": "user not found",
	})
}
func createUser(c *gin.Context) {
	var newUser User
	err := json.NewDecoder(c.Request.Body).Decode(&newUser)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{
			"message": "invalid data",
		})
		return
	}
	users = append(users, newUser)
	c.JSON(http.StatusCreated, newUser)
}
func updateUser(c *gin.Context) {
	id, _ := strconv.Atoi(c.Param("id"))
	var updatedUser User
	err := json.NewDecoder(c.Request.Body).Decode(&updatedUser)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{
			"message": "invalid data",
		})
		return
	}
	for index, user := range users {
		if user.ID == id {
			users[index] = updatedUser
			c.JSON(http.StatusOK, updatedUser)
			return
		}
	}
	c.JSON(http.StatusNotFound, gin.H{
		"message": "user not found",
	})
}
func deleteUser(c *gin.Context) {
	id, _ := strconv.Atoi(c.Param("id"))
	for index, user := range users {
		if user.ID == id {
			users = append(users[:index], users[index+1:]...)
			c.JSON(http.StatusOK, gin.H{
				"message": "user deleted",
			})
			return
		}
	}
	c.JSON(http.StatusNotFound, gin.H{
		"message": "user not found",
	})
}

func main() {
	r := gin.Default()
	r.GET("/users", getUsers)
	r.GET("/users/:id", getUser)
	r.POST("/users", createUser)
	r.PUT("/users/:id", updateUser)
	r.DELETE("/users/:id", deleteUser)
	r.Run(":8080")
}